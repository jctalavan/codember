def killMecenas(mecenas: list) -> list:

    if len(mecenas) == 1:
        return mecenas

    int indice = 0;

    if len(numbers) % == 0:
        while indice < len(numbers):
            survivors.append(numbers[indice])
            indice+=2

    else:
        survivors.append(numbers(-1))
        while indice < len(numbers) - 1:
            survivors.append(numbers[indice])
            indice+=2

    return survivors

if __name__ == "__main__":

    mecenas = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    while len(mecenas) > 1:
        mecenas = killMecenas(mecenas)

    print(mecenas[0])