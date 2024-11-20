import os
import io


# Чтобы не творить хаос в основной директории, все txt файлы были помещены в директорию Module_7_3_files
# Далее работа с файлами будет производиться именно из этой папки
# В связи с этим класс WordsFinder будет принимать названия файлов с папкой, чтобы напрямую подставлять в open
# Логика несколько изменена. В объект передаются папки, а файлы уже ищутся сами

class WordsFinder:
    def __init__(self, *args):
        self.file_folders = args
        self.all_words = {}
        pass

    def get_all_words(self):
        # fold_name = 'Module_7_3_files'
        punct = [',', '.', '=', '!', '?', ';', ':', '— ', '\"']
        for folder in self.file_folders:
            files_list = os.listdir(folder)
            for file_txt in files_list:
                with open(os.path.join(folder, file_txt), 'r', encoding='utf-8') as file:
                    lines = file.readlines()  # Считываем все строки в список и закрываем файл
                words = []
                for line in lines:
                    line = line.strip().casefold()  # Убираем символы переноса и пробелы по бокам нижний регистр
                    for sign in punct:  # Удаляем символы пунктуации
                        line = line.replace(sign, '')
                    for word in line.split():
                        words.append(word)
                self.all_words[os.path.join(folder, file_txt)] = words

    def print_wrds(self):
        for file, words in self.all_words.items():
            print(f'Path: {os.path.split(file)[0]}')
            print(f'File: {os.path.split(file)[1]}')
            print(f' Words: {words}') if words else print('No words')
            print()



finder =  WordsFinder('Module_7_3_files', 'Module_7_3_morefiles')
finder.get_all_words()
# for file, words in finder.all_words.items():
#     print(f'Path: {os.path.split(file)[0]}')
#     print(f'File: {os.path.split(file)[1]}')
#     print(f' Words: {words}')
#     print()

finder.print_wrds()
