import re


def calcMolecularMass(substance:str) -> int:
    """
    Рассчитывает молекулярную массу вещества
    """
    massOfElements = {'C':12, 'H':1, 'O':16, 'N':14, 'Al':23}

    pattern = r'(C|H|O|N|Al)(\d*)'     # * - указывает, что символ может встречаться 0 или более раз
    matches = re.findall(pattern, substance)   # ищет ВСЕ совпадения

    mass =0

    for match in matches:
        element = match[0]
        numOfElement = int(match[1] or 1)
        mass += massOfElements[element]*numOfElement
    return mass



s = "C2H5OHMg"
print(calcMolecularMass(s))

s = "C6H12O6"
print(calcMolecularMass(s))

s = "NH2-CH-CH3-COOH"
print(calcMolecularMass(s))