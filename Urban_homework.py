calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_of_str):
    count_calls()
    return any(string.lower() == str_of_list.lower() for str_of_list in list_of_str)


# Вызовем сразу несколько раз string_info
for i in 'каприз клоун колба колун крона уклон колыбель карта'.split():
    print(string_info(i))
print()
# Возьмем те же слова для is_contains
for j in 'каприз клоун лопата сережка колыбель стружка орден'.split():
    print(f'Слово "{j}" находится в списке') if is_contains(j, 'каприз клоун колба колун крона уклон колыбель карта'.split()) else print(f'Слова "{j}" в списке нет')
print()

print(f'Всего запросов фукций: {calls}')
