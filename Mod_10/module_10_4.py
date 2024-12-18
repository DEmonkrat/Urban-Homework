import threading
from time import sleep
from queue import Queue
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __bool__(self):  # Если стол пуст, вернет False, если занят, то True
        if self.guest is None:
            return False
        else:
            return True


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        guests = list(guests)
        for i in range(len(self.tables)):  # Пробегаемся по всем столам и ...
            if self.tables[i].guest is None:  # если стол свободен, то ...
                self.tables[i].guest = guests.pop()  # сажаем гостя за стол и убираем его из списка гостей, ...
                print(
                    f'{self.tables[i].guest.name} сел за стол номер {self.tables[i].number}')  # выводим сообщение, ...
                self.tables[i].guest.start()  # запускаем поток (таймер) гостя.
            if not guests:  # Завершаем цикл for, если гостей больше нет
                break
        if guests:  # Если не всех гостей рассадил, то ...
            for _ in range(len(guests)):
                guest = guests.pop()  # убираем гостя из списка гостей, ...
                self.queue.put(guest)  # помещаем в очередь ...
                print(f'{guest.name} в очереди')  # выводим сообщение.

    def serv_guests(self):
        while not self.queue.empty() or any(self.tables):  # Проверяем на не пустую очередь или не пустые столы
            for i in range(len(self.tables)):
                if not self.tables[i].guest.is_alive():
                    self.tables[i].guest = None
                    print(f'{self.tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables[i].number} свободен')
                    if not self.queue.empty():
                        self.tables[i].guest = self.queue.get()
                        print(
                            f'{self.tables[i].guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}')
                        self.tables[i].guest.start()
        print('Всех обслужили !!!')


guests_list = [Guest('Anton'), Guest('Petya'), Guest('Nina'), Guest('Michel'), Guest('Dima'), Guest('Ksyusha'),
               Guest('Masha'), Guest('Alexander')]
tables_list = [Table(1),Table(2),Table(3)]

shokoladnica = Cafe(*tables_list)
shokoladnica.guest_arrival(*guests_list)
shokoladnica.serv_guests()