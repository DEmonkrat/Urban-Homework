def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for count, string in enumerate(strings):
            position = file.tell()
            file.write(string + '\n')
            strings_positions[(count + 1, position)] = string
    return strings_positions

def custom_write_close(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for count, string in enumerate(strings):
        position = file.tell()
        file.write(string + '\n')
        strings_positions[(count + 1, position)] = string
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

print('Другой вариант')

result2 = custom_write_close('test.txt', info)
for elem in result2.items():
    print(elem)
