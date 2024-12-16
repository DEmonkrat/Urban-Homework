import threading, time
from random import randint

class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            withdraw = randint(50, 500)
            self.balance += withdraw
            print(f'Пополнение на: {withdraw}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                print('Поток разблокирован')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            removal = randint(50, 500)
            print(f'Запрос на снятие: {removal}')
            if (self.balance - removal) >= 0:
                self.balance -= removal
                print(f'Снятие: {removal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                print('Поток заблокирован')
            time.sleep(0.001)



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
