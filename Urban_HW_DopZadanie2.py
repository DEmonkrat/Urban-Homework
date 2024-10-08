n = 1
while not (3 <= n <= 20):
    n = int(input('Введите целое число от 3 до 20 (включительно): '))
print()
print(f'Найдем все пары для {n}')
result = ''
for i in range(1, n):
    for j in range(i + 1, n):  # Начиная вложенный цикл с (i + 1) мы искоючаем появление зеркальных пар в result
        if n % (i + j) == 0: result += str(i) + str(j)
print(f'Парами для {n} являются {result}')
