from decimal import *
def add_everything_up(a, b):
    try:
        a + b
        return Decimal(str(a)) + Decimal(str(b))
    except TypeError:
        print('Не все элементы числа, поэтому используем конкатенацию: ')
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# print(Decimal('123.456'))