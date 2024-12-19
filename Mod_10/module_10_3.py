import threading, time
from random import randint


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()  # Экземпляр класса Лок для блокировки снятия
        self.b_lock = threading.Lock()  # Экземпляр класса Лок для блокировки операций со счетами/балансом

    def deposit(self):
        for _ in range(100):
            refill = randint(50, 100)  # Специально поменьше сделал, чтобы точно срабатывала блокировка
            self.__bal_change(refill)
            if self.__bal_check() >= 500 and self.lock.locked():
                self.lock.release()
                print('Поток разблокирован')
            time.sleep(0.001)
        if self.lock.locked():
            self.lock.release()  # Отпускаем замок, если исчерпали range и замок заблокирован
            print('Поток разблокирован')
            print('Поток пополнения иссяк (((')

    def take(self):
        for _ in range(100):
            removal = randint(50, 500)
            print(f'Запрос на снятие: {removal}')
            if (self.__bal_check() - removal) >= 0:
                self.__bal_change(-removal)
            else:
                print('Запрос отклонён, недостаточно средств')
                if threading.active_count() > 2:    # Ставим замок только если есть поток пополнения (т.е. их больше 2)
                    self.lock.acquire()
                    print('Поток заблокирован. Потоков:', threading.active_count())
            time.sleep(0.001)
        print('Поток снятия иссяк !!!')

    def __bal_check(self):
        with self.b_lock:
            return self.balance

    def __bal_change(self, by):
        with self.b_lock:
            self.balance += by
            if by > 0:
                print(f'Пополнение на: {by}. Баланс: {self.balance}')
            else:
                print(f'Снятие: {by}. Баланс: {self.balance}')


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,), name='refill')
th2 = threading.Thread(target=Bank.take, args=(bk,), name='removal')

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
