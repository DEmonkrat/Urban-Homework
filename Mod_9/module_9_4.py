import os
from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))


# Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='UTF-8') as file:
            if data_set:
                for element in data_set:
                    file.write(str(element) + '\n')

    return write_everything


name_f: str = 'example_file.txt'
full_write = get_advanced_writer(name_f)
full_write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# os.remove(name_f)

# Метод __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        if len(self.words):
            return choice(self.words)


mball = MysticBall('Да', 'Нет', 'Наверное')
print(mball())
