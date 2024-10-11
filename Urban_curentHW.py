# Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c, sep='\n')
    print()


print_params()
print_params(4)
print_params([1, 2, 3], c=False)
print_params(c='тоже строка')
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров:
values_list = [23, 'string', [4, 5, 6]]
values_dict = {'a': 44, 'b': [33, 'list'], 'c': 'fruit'}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры:
values_list_2 = [False, (1941, 1945)]
print_params(*values_list_2, 42)
print('Все работает :)')