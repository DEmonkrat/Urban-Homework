from decimal import *


def add_everything_up(a, b):
    try:
        a + b   # Пробуем сложить, если не получается, значит есть строки ...
        return Decimal(str(a)) + Decimal(str(b))    # .. если получается, то используем Decimal для точности
    except TypeError:
        print('Не все элементы числа, поэтому используем конкатенацию: ')
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
