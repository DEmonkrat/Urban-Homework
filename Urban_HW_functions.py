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
