import requests
import json

class Mecena:
    def __init__ (self, initial_position, name):
        # self allows to attach parameter to the class
          self.initial_position = initial_position
          self.name = name

def killitems(items: list) -> list:

    if len(items) == 1:
        return items

    position = 0
    survivors = list()

    if len(items) % 2 == 0:
        while position < len(items):
            survivors.append(items[position])
            position+=2

    else:
        survivors.append(items[-1])
        while position < len(items) - 1:
            survivors.append(items[position])
            position+=2

    return survivors

if __name__ == "__main__":

    # items = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

    response = requests.get('https://codember.dev/mecenas.json')
    items = json.loads(response.text.replace('\n',''))

    mecenas = list()
    for index, item in enumerate(items):
        mecena = Mecena(index, item)
        mecenas.append(mecena)

    while len(mecenas) > 1:
        mecenas = killitems(mecenas)

    print(f"{mecenas[0].name}-{mecenas[0].initial_position}")