# https://github.com/DEmonkrat/Urban-Homework/blob/main/Urban_HW_DopZadanie2.py
n = 1
while not (3 <= n <= 20):
    n = int(input('Введите целое число от 3 до 20 (включительно): '))
print()
print(f'Найдем все пары для {n}')
result = ''
for i in range(1,n//2 + 1): # Смотрим до половины т.к. остальное зеркала (сокращаем цикл)
  for j in range(n - i, i, -1): # Идем в обратную сторну с учетом предыдущих значений (сокращаем цикл)
        if n % (i + j) == 0: result += str(i) + str(j)
print(f'Парами для {n} являются {result}')
