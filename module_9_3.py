import time
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Решил проверить скорость выполнения сборок и list cmop-n. На лекциях утверждали, что сборки еще и быстрее,
# но на практике этого не видно. Получается основная разница это объем занимаемой памяти
start_time_g = time.time()
for _ in range(10000):
    first_result = (len(x) - len(y) for x,y in zip(first, second))
    list(first_result)
end_time_g = time.time()
print(f'Время (генераторная сборка): {end_time_g - start_time_g}')

start_time_l = time.time()
for _ in range(10000):
    first_result_list = [len(x) - len(y) for x,y in zip(first, second)]
end_time_l = time.time()
print(f'Время (списковая сборка): {end_time_l - start_time_l}')

# Теперь по заданию :)
start_time_g1 = time.time()
for _ in range(10000):
    first_result = (len(x) - len(y) for x,y in zip(first, second) if len(x) != len(y))
    list(first_result)
end_time_g1 = time.time()
print(f'With ZIP: {end_time_g1 - start_time_g1}')
first_result = (len(x) - len(y) for x,y in zip(first, second) if len(x) != len(y))
print(list(first_result))

start_time_g2 = time.time()
for _ in range(10000):
    second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
    list(second_result)
end_time_g2 = time.time()
print(f'Without ZIP: {end_time_g2 - start_time_g2}')
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
print(list(second_result))
# Здесь особой разницы по длительности не видно
