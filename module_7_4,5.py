# Форматирование строк (НИЖЕ Файлы в операционной системе)
# Использование %
team1_num = 5
print('В команде Мастера кода участников: %s!' % team1_num)
team1_num, team2_num = 6, 7
print('Итого сегодня в командах участников: %s и %s !' %  (team1_num, team2_num))

# Использование format()
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = 18015.2
print('Волшебники данных решили задачи за {time} с' .format(time= team1_time))

# Использование f-строк
score_1, score_2 = 40, 42
team2_time = 1769.4
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}!')
tasks_total = sum([score_1, score_2])
time_avg = sum([team1_time, team2_time])/tasks_total
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg:.2f} секунды на задачу!')

# Файлы в операционной системе
print(chr(356))