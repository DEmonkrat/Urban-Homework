import os.path

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_product_l(self):  # Считывает и возвращает содержимое файла списком
        prod_list = []
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, 'r')  # Файл в режиме чтения
            prod_list = file.readlines()
            file.close()
            if prod_list:  # Если список из файла не пуст, то удаляем \n
                prod_list = list(map(str.strip, prod_list))
        else:
            print(f'Файл с именем {self.__file_name} отсутствуйте')
        return prod_list

    def get_products(self):  # Считывает и возвращает содержимое файла одной строкой
        prod_str = ''
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name, 'r')  # Файл в режиме чтения
            prod_str = file.read()
            file.close()
        else:
            print(f'Файл с именем {self.__file_name} отсутствуйте')
        return prod_str

    def __set_of_prod(self):  # Формирует множество из названий продуктов (из списка)
        prod_list = self.get_product_l()
        return set([prod.split(',')[0].casefold() for prod in prod_list])

    def add_p(self, *products):
        file = open(self.__file_name, 'a')  # Файл в режиме добавления
        if products:  # Если есть что добавлять, то пытаемся добавить (если нет, создаем пустой файл)
            set_of_prod = self.__set_of_prod()  # Формируем множество названий продуктов
            for item in products:
                if not item.name.casefold() in set_of_prod:  # Если названия нет в множестве продуктов, то ...
                    file.write(str(item) + '\n')  # ... пишем в файл и добавляем в множество
                    set_of_prod.add(item.name.casefold())
                else:
                    print(f'Продукт {item.name} уже есть в магазине')
        file.close()

    def clr_file(self):
        if os.path.isfile(self.__file_name):
            open(self.__file_name, 'w').close()
        else:
            print(f'Файл с именем {self.__file_name} отсутствуйте')


p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
o1 = Product('Orange', 10.1, 'Fruit')
o2 = Product('Lemon', 5., 'Fruit')

# Перед проверками лучше удалить файл products.txt, т.к. несколько проверок рассчитаны на его отсутствие
print('Выводим информацию об Продуктах (не всех)')
print(str(p1))
print(str(p2))
print(str(p3))
print()

shop1 = Shop()

print('Проверяем при отсутствии файла:')
print(shop1.get_product_l())
print(shop1.get_products())

shop1.add_p()   # Создаем пустой файл
print('Проверяем при наличии пустого файла:')
print(shop1.get_product_l())
print(shop1.get_products())

# shop1.clr_file()  # Очищаем файл, иначе там очень много всего будет за время тестирования :-)
print('Добавляем продукты в файл')
shop1.add_p(p1, p2, p3, o1, o2, p1, p2, p3, o1, o2)
print()
print('Добавили (если отсутствовал). Теперь считаем файл')
print('Список продуктов в магазине:\n', shop1.get_product_l(), sep='')
print()

print('Возвращаем содержимое файла одной строкой')
print(shop1.get_products())