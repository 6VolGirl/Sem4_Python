import re
import sys
sys.path.append(r'C:\Users\6anna\PycharmProjects\Sem4_Laba1')

#from Task2 import romToDec
class ZeroDivisionError(Exception):
    """Исключение для деления на ноль"""
    def __init__(self, message="Римские числа не могут быть отрицательными"):
        super().__init__(message)

class RomanNumbersMinus(Exception):
    """Исключение для отрицательных римских чисел"""
    def __init__(self, message="Римские числа не могут быть отрицательными"):
        super().__init__(message)

class RomanNumbersDivisionError(Exception):
    """Исключение для нецелочисленного деления римских чисел"""
    def __init__(self, message="Деление римских чисел привело к нецелому результату"):
        super().__init__(message)


class RomanNumber:
    def __init__(self, number):
        if isinstance(number, str):    #проверка типа
            self.roman_num = number
            self.arab_value = RomanNumber.romToDec(number)
        if isinstance(number, int):
            self.arab_value = number
            self.roman_num = RomanNumber.decToRom(number)

    def __repr__(self):
        return f'{self.roman_num} is {self.arab_value}'

    def __str__(self):
        return self.roman_num

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.arab_value + other.arab_value)
        if isinstance(other, int):
            return  RomanNumber(self.arab_value + other)

    def __radd__(self, other):
        return RomanNumber(self.arab_value + other)

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.arab_value - other.arab_value)
        if isinstance(other, int):
            return RomanNumber(self.arab_value - other)

    def __rsub__(self, other):
        return RomanNumber(other - self.arab_value)

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(other.arab_value *self.arab_value)
        if isinstance(other, int):
            return RomanNumber(other * self.arab_value)

    def __rmul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(other.arab_value *self.arab_value)
        if isinstance(other, int):
            return RomanNumber(other * self.arab_value)

    def __pow__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.arab_value ** other.arab_value)
        if isinstance(other, int):
            return RomanNumber(self.arab_value ** other)

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            if other.arab_value == 0:
                raise ZeroDivisionError("Деление на ноль")
            if self.arab_value % other.arab_value != 0:
                raise RomanNumbersDivisionError("Деление римских чисел привело к нецелому результату")
            return RomanNumber(self.arab_value // other.arab_value)

        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль")
            if self.arab_value % other != 0:
                raise RomanNumbersDivisionError("Деление римских чисел привело к нецелому результату")
            return RomanNumber(self.arab_value // other)
        return NotImplemented

    def __truediv__(self, other):
       #return self.__floordiv__(other)
       raise RomanNumbersDivisionError("Деление римских чисел не поддерживается.")

    def __eq__(self, other):
        if isinstance(other, RomanNumber):
             return self.roman_num == other.roman_num
        elif isinstance(other, int):
             return self.roman_num == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.roman_num < other.roman_num
        elif isinstance(other, int):
            return self.roman_num < other
        return NotImplemented

    def __neg__(self):
        raise RomanNumbersMinus()

    def __int__(self):
        return self.roman_num

    def is_even(self):
        return self.arab_value % 2 == 0

    def next(self):
        return RomanNumber(self.arab_value + 1)

    def prev(self):
        if self.arab_value - 1 < 1:
            raise RomanNumbersMinus("Римские числа не могут быть меньше I (1)")
        return RomanNumber(self.arab_value - 1)


    def romToDec(roman_num: str) -> int:
        """
        Переводит строку с римскими числами в обычные десятичные.
        """
        romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        if not re.match(pattern, roman_num):
            print('Invalid string of rom')
            return 0

        resultNum = 0
        valuePrevious = 0
        for char in roman_num[::-1]:
            value = romanValues[char]
            if value < valuePrevious:
                resultNum -= value
            else:
                resultNum += value
            valuePrevious = value

        return resultNum


    def decToRom(dec: int):
        roman = ""
        roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for value, symbol in roman_numerals:
            while dec >= value:
                roman += symbol
                dec -= value
        return roman



a = RomanNumber('X')
b = RomanNumber('III')

print(a + b)
print(a - b)
print(a * b)

print(RomanNumber('X') == RomanNumber('X'))
print(RomanNumber('X') > RomanNumber('V'))

print(a.is_even())
print(b.is_even())

print(a.next())
print(a.prev())


