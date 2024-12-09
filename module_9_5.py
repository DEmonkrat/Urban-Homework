class StepValueError(ValueError):
    pass


class StartStopValueError(ValueError):
    pass

class Iterator:
    def __init__(self, stop, start=0, step=1):  # Сделал как в range
        self.stop = stop
        self.start = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        else:
            self.step = step
        if (self.step > 0 and self.stop <= self.start) or (self.step < 0 and self.stop >= self.start):
            raise StartStopValueError('Неверные границы последовательности')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer <= self.stop:
            return self.pointer
        elif self.step < 0 and self.pointer >= self.stop:
            return self.pointer
        else:
            print('Конец последовательности')
            raise StopIteration


iter1 = Iterator(10)
for num in iter1:
    print(num)

iter10 = Iterator(100, 0, 10)
for num in iter10:
    print(num)

iter11 = Iterator(-50, 100, -25)
for num in iter11:
    print(num)

# Далее идут Итераторы с ошибками
iter2 = Iterator(10, 20)
for num in iter2:
    print(num)

iter3 = Iterator(20, 10, -1)
for num in iter3:
    print(num)

iter4 = Iterator(20, 10, 0)
for num in iter4:
    print(num)