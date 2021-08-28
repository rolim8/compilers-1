def toInt(stringToInt):
    stringToInt = input('Digite um valor: ')
    print(type(stringToInt))

    try:
        return int(stringToInt)
    except ValueError:
        return float(stringToInt)