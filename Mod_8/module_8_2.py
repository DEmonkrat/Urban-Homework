def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    num_count = 0
    summ = 0
    try:
        summ, incorrect = personal_sum(numbers)
        num_count = len(numbers) - incorrect
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        return summ/num_count
    except ZeroDivisionError:
        return 0


elements1 = [1, 4, 10, 'tt', (6, 7), ['rty', '6789'], 67]
elements2 = []
elements3 = 'sdfgfds23'
print('elements1: ', personal_sum(elements1))
print('elements2: ', personal_sum(elements2))
print('elements3: ', personal_sum(elements3))
print()

print('________________________________Из задания_________________________________________')
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
