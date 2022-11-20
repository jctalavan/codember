import requests
import json

def process_colors(colors) -> str:

    current = list()
    max = list()
    color_a = ""
    color_b = ""
    compare_to = 0

    for color in colors:
        
        if(color_a == ""):
            color_a = color
            current.append(color)
            continue

        if(color_b == ""):
            
            if(color == color_a):
                continue
            
            color_b = color
            current.append(color)
            continue

        if(compare_to == 0 and color == color_a):
            current.append(color)
            compare_to = 1
        elif(compare_to == 1 and color == color_b):
            current.append(color)
            compare_to = 0
        else:
            if(len(current) >= len(max)):
                max = current.copy()
                
            color_a = current[-1]
            color_b = color
            current.clear()
            current.append(color_a)
            current.append(color_b)
            compare_to = 0

    if(len(current) >= len(max)):
        max = current.copy()

    return f"{len(max)}@{max[-1]}"

if __name__ == "__main__":

    # colors = ['red', 'blue', 'red', 'blue', 'green'] #-> 4, blue
    # colors = ['green', 'red', 'blue', 'gray'] #-> 2, gray
    # colors = ['blue', 'blue', 'blue', 'blue'] #-> 1, blue
    # colors = ['red', 'green', 'red', 'green', 'red', 'green'] #-> 6, green
    # colors = ['blue', 'red', 'blue', 'red', 'gray'] #-> 4, red
    # colors = ['red', 'red', 'blue', 'red', 'red', 'red', 'green'] #-> 3, red
    # colors = ['red', 'blue', 'red', 'green', 'red', 'green', 'red', 'green'] #-> 6, green

    response = requests.get('https://codember.dev/colors.txt')
    
    # Convert data to dict
    colors = json.loads(response.text.replace('\n',''))
 
    print(process_colors(colors))