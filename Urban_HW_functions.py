# Task 1
def outer_f(inner_fun):
    text = inner_fun('Hi there')
    print(text)


def upper_inner_f(text):
    return text.upper()


outer_f(upper_inner_f)


# Task 2
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or \
            '@' not in sender or \
            (not recipient.endswith('.com') and not recipient.endswith('.ru') and not recipient.endswith('.net')) or \
            (not sender.endswith('.com') and not sender.endswith('.ru') and not sender.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender == recipient:
        print('Нельзя отправлять самому себе')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


mails = [['asdfsdf', 'dima.com', None],
         ['ljkhlkjh', 'banket@mail', None],
         ['xzcvxcz', 'dima@mail.ru', 'urban@yandex'],
         ['zxcvzxcv', 'university.help@gmail.com', ''],
         ['uyr', 'dima@mail.ru', None],
         ['uyr', 'dima@mail.ru', 'alina@yandex.com']]

for mail in mails:
    send_email(mail[0], mail[1], sender=mail[2]) if mail[2] else send_email(mail[0], mail[1])


# Task 3
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


#Task 4
#Произвольное число параметров
def single_root_words(root_word, *other_words):
  same_words = []
  for word in other_words:
    if (root_word.lower() in word.lower()) or (word.lower() in root_word.lower()): same_words.append(word)
  return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


#Task 5 (special)
#Специальное задание по рекурсии
def flat_list_sum(list_):
    # Если передан список/кортеж, то раскрываем
    if isinstance(list_, (list, tuple)):

        if len(list_) == 0:
            return 0  # Если дошли до конца, вернуть ноль

        if isinstance(list_[0], (int, float)):  # Если элемент списка число/булево, возвращаем его и идем дальше
            return list_[0] + flat_list_sum(list_[1:])

        if isinstance(list_[0], str):  # Если элемент списка строка, возвращаем ее длину и идем дальше
            return len(list_[0]) + flat_list_sum(list_[1:])

        if isinstance(list_[0], (list, tuple)):  # Если элемент списка список или кортеж - раскрываем его и смотрим дальше
            return flat_list_sum(list_[0]) + flat_list_sum(list_[1:])

        if isinstance(list_[0],
                      set):  # Если элемент списка множество - перевести в список, раскрыть его и смотрим дальше
            return flat_list_sum(list(list_[0])) + flat_list_sum(list_[1:])

        if isinstance(list_[0], dict):
            key_sum, value_sum = 0, 0
            for key, value in list_[0].items():
                key_sum += flat_list_sum(key)
                value_sum += flat_list_sum(value)
            return key_sum + value_sum + flat_list_sum(list_[1:])
        else:
            return 0  # Для типа данных None (если часть списка)

    # Если передано число/строка/словарь, то считаем и выдаем.
    # Если множество, то в словарь и раскрываем
    if isinstance(list_, (int, float)):  # Если элемент число/булево, возвращаем его
        return list_

    if isinstance(list_, str):  # Если элемент строка, возвращаем ее длину
        return len(list_)

    if isinstance(list_, dict):  # Если словарь, то считаем его
        key_sum, value_sum = 0, 0
        for key, value in list_.items():
            key_sum += flat_list_sum(key)
            value_sum += flat_list_sum(value)
        return key_sum + value_sum

    if isinstance(list_, set):  # Если элемент множество - перевести в список, раскрыть его и смотрим дальше
        return flat_list_sum(list(list_))
    else:
        return 0  # Для типа данных None

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': None}, 8),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(flat_list_sum(data_structure))