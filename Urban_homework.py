def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or \
            '@' not in sender or \
            (not recipient.endswith('.com') and
             not recipient.endswith('.ru') and
             not recipient.endswith('.net')) or \
            (not sender.endswith('.com') and
             not sender.endswith('.ru') and
             not sender.endswith('.net')):
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
