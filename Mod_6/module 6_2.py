class Vehicle:
    __COLOR_VARIANTS = ['red', 'green', 'blue', 'dark', 'black', 'grey', 'silver', 'cherry', 'white', 'lime', 'yellow',
                        'orange', 'violet', 'purple']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.casefold() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


sed_1 = Sedan('Ivan I', 'Lancer', 125, 'green')
print()
sed_1.print_info()
print('____Теперь по отдельности____')
print(sed_1.get_model())
print(sed_1.get_horsepower())
print(sed_1.get_color())
print('____Пробуем изменить цвет на lite_dark____')
sed_1.set_color('lite_dark')
print('____Пробуем изменить цвет на black____')
sed_1.set_color('black')
print(sed_1.get_color())
print('____Пробуем изменить владельца____')
sed_1.owner = 'Dmitry M'
sed_1.print_info()
