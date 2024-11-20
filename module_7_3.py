import os


# Чтобы не творить хаос в основной директории, все txt файлы были помещены в директорию Module_7_3_files
# Логика несколько изменена. В объект передаются папки, а файлы уже ищутся сами
# UPDT. Логика расширена: класс принимает папки и названия фалов (из основной директории)
# Таким образом полностью выполняются условия основного задания

class WordsFinder:
    def __init__(self, *args):
        self.file_folders = []
        self.files = []
        # Далее распределяем файлы и папки по двум спискам
        for arg in args:
            if arg.endswith('.txt'):
                self.files.append(arg)
            else:
                self.file_folders.append(arg)
        self.all_words = {}
        pass

    def get_all_words(self):
        for folder in self.file_folders:
            if os.path.isdir(folder):  # Проверка на существование каталога
                files_list = os.listdir(folder)  # Делаем список файлов в директории
                for i in range(len(files_list)):
                    files_list[i] = os.path.join(folder, files_list[i])  # Соединяем название файла с директорией
                files_list.extend(self.files)  # Соединяем со списком файлов в основной директории
                files_list = set(files_list)  # Убираем дубли, если есть
                # После всего получаем единый кортеж типа 'директория\файл' или 'файл' (если в основной папке)
                # И то, и другое пригодно для передачи в функцию open в текущем виде (для этого все и делалось)
                self.__find_in(files_list)  # Для поиска и обработки слов написана отдельная служебная функция


    def __find_in(self, fnd_lst):
        punct = [',', '.', '=', '!', '?', ';', ':', '— ', ' -', '\"']
        for file_txt in fnd_lst:
            if os.path.isfile(file_txt):  # Проверка на существование файла
                with open(file_txt, 'r', encoding='utf-8') as file:
                    lines = file.readlines()  # Считываем все строки в список и закрываем файл
                words = []
                for line in lines:
                    line = line.strip().casefold()  # Убираем символы переноса и пробелы по бокам нижний регистр
                    for sign in punct:  # Удаляем различные символы
                        line = line.replace(sign, '')
                    for word in line.split():
                        words.append(word)
                self.all_words[file_txt] = words


    def print_words(self):
        for file, words in self.all_words.items():
            print(f'File: {os.path.split(file)[1]}')
            print(f'Path: \\{os.path.split(file)[0]}') if os.path.split(file)[0] else print('Path: MAIN DIR')
            print(f' Words: {words}') if words else print('No words')
            print()



# Для проверки работы всех ф-ций класса, вводим существующие и несуществующие папки и файлы
finder =  WordsFinder('Module_7_3_files', 'Module_7_3_morefiles', 'text_main.txt', 'no_catalog', 'no_file.txt', 'no_file.exe')
finder.get_all_words()
finder.print_words()
