import os
import shutil

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
print(end='\n\n\n')

# Следующее домашнее задание !!!
# Файлы в операционной системе
def print_size(size, name=''):
    print('Название файла: ', name)
    if size//10**3 < 1:
        print(f'Размер файла: {size} байт')
    elif size//10**6 < 1:
        print(f'Размер файла: {size//10**3:.2f} Кбайт')
    else:
        print(f'Размер файла: {size//10**6:.2f} Мб')
    print()


print('Метод OS.WALK')
directory = '.'
for cur_dir, dirs, files in os.walk(directory):
    print(f'Текущий каталог: {os.path.join(os.getcwd(), cur_dir[2:])}')
    print(f'Подкаталоги: ', end='')
    if not dirs:
        print('пусто')
    elif len(dirs) < 8:
        print(*dirs, sep=', ')
    else:
        print(*dirs[:5],  ' ... ', dirs[-1] , sep=', ', end='')
        print(' | Всего каталогов: ', len(dirs))
    print('Файлы: ', end='')
    if not files:
        print('пусто', end='\n\n')
    elif len(files) < 8:
        print(*files, sep=', ', end='\n\n')
    else:
        print(*files[:5],  ' ... ', files[-1] , sep=', ', end='')
        print(' | Всего файлов: ', len(files), end='\n\n')

import time
print('Метод os.path.getmtime')
file_name = 'module_4_1.py'
file_time = time.localtime(os.path.getmtime(file_name))
print(f'Время последней модификации файла "{file_name}":')
print(*file_time[:3], sep='-', end=' ')
print(*file_time[3:6], sep=':')
file_size = os.path.getsize(file_name)
with open('test_size.txt', 'w') as f:
    f.write('test_size'*10**3)

print_size(file_size, file_name)
print_size(os.path.getsize('test_size.txt'), 'test_size.txt')
print()
print('Теперь увеличим размер файла')
with open('test_size.txt', 'w') as f:
    f.write('test_size'*10**6)
print_size(os.path.getsize('test_size.txt'), 'test_size.txt')
# Между прочим винда пишет 8.790 Мб
# Удалим наш БОЛЬШОЙ файл
os.remove('test_size.txt')

print('Метод os.path.dirname')
# Создаем папку с файлом
os.makedirs(r'Test_dir\file.txt')
print(os.path.dirname(r'Test_dir\file.txt'))
# Удаляем папку со всем содержимым
shutil.rmtree('Test_dir')