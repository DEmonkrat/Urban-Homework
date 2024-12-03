class IncorrectVinNumber(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class IncorrectCarNumbers(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.vin_number = vin_number
        if self.__is_valid_numbers(numbers):
            self.numbers = numbers

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер', vin_number)
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров', numbers)
        elif len(numbers) != 6:
            raise IncorrectVinNumber('Неверная длина номера', numbers)
        else:
            return True


try:  # проверяем VIN
    car1 = Car('Forester', 213456, '456789')
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()
else:
    print('Создали первую машину )')

try:
    car1 = Car('Forester', 2134.56, '456789')
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()

try:  # проверяем VIN
    car1 = Car('Forester', '213456', '456789')
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()
else:
    print('Создали первую машину )')

try:  # проверяем номера
    car1 = Car('Forester', 1324657, 456789)
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()
else:
    print('Создали первую машину )')

try:  # проверяем номера
    car1 = Car('Forester', 1324657, '453456789')
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()
else:
    print('Создали первую машину )')

try:
    car1 = Car('Forester', 1324657, '453459')
except IncorrectVinNumber as exc:
    print(f'Сообщение об ошибке: {exc.message}')
    print(f'Переданные данные: {exc.extra_info} ({type(exc.extra_info)})')
    print()
else:
    print('Создали первую машину )')
    print(car1.model)