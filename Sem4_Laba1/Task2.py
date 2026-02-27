import re  #регулярные выражения


def checkStr(rom: str) -> bool:
    """
    Проверяет форму строки.
    """
    pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, rom))


def romToDec (rom: str) -> int:
    """
    Переводит строку с 16-ричными числами в обычные десятичные.
    """
    romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not checkStr(rom):
        print('Invalid string of rom')
        return 0

    resultNum = 0
    valuePrevious = 0
    for char in rom[::-1]:
        value = romanValues[char]
        if value<valuePrevious:
            resultNum -= value
        else:
            resultNum += value
        valuePrevious = value

    return resultNum



s = "LVIII"
print (romToDec (s))

s = "MCMXCIV"
print (romToDec (s))

s = "MMILC"
print (romToDec (s))