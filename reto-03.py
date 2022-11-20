import requests

def process_colors(colors) -> str:

    zebra_colors = ["", ""]
    current_counter = 0
    max_counter = 0
    compare_to = 0
    last_zebra_color = ""

    for color in colors:
        if(zebra_colors[0] == ""):
            zebra_colors[0] = color
            current_counter = 1
            last_zebra_color = color
            continue

        if(zebra_colors[0] != "" and zebra_colors[1] == ""):
            if(zebra_colors[0] == color):
                continue
            else:
                zebra_colors[1] = color
                current_counter = 2
                last_zebra_color = color
                continue

        if(compare_to == 0):
            if(zebra_colors[0] == color):
                current_counter += 1
                last_zebra_color = color
                compare_to = 1
            else:
                if(current_counter > max_counter):
                    max_counter = current_counter
                
                zebra_colors[0] = zebra_colors[1]
                zebra_colors[1] = color
                current_counter = 2
        else:
            if(zebra_colors[1] == color):
                current_counter += 1
                last_zebra_color = color
                compare_to = 0
            else:
                if(current_counter > max_counter):
                    max_counter = current_counter

                zebra_colors[0] = zebra_colors[1]
                zebra_colors[1] = color
                current_counter = 2

    if(max_counter == 0):
        max_counter = current_counter

    return f"{max_counter}@{last_zebra_color}"

if __name__ == "__main__":

    # response = requests.get('https://codember.dev/colors.txt')
    # colors = response.text

    colors = ['green', 'red', 'blue', 'gray']
    print(process_colors(colors))