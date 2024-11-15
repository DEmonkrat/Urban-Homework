# __________________Figure_________________________
class Figure:
    SIDES_COUNT = 0

    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        # Служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
        arg_bool = True
        for side in args:
            if (side < 0) or (not isinstance(side, int)) or (len(args) != self.SIDES_COUNT):
                arg_bool = False
                break
        return arg_bool

    def check_valid_sides(self, *args):
        return self.__is_valid_sides(*args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        pass

    def set_sides(self, *new_sides):
        if len(new_sides) == self.SIDES_COUNT:
            self.__sides = list(new_sides)
        else:
            print(f'Введено неверное кол-во сторон. Должно быть {self.SIDES_COUNT}')


# __________________Circle_________________________
class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, sides, color, filled):
        from math import pi
        super().__init__(sides, color, filled)
        if self.check_valid_sides(self.get_sides()[
                                      0]):  # проверяем только первый (у круга одна сторона), если остальные есть (и даже с ошибками), то нам это не интересно
            self.__radius = self.get_sides()[0] / (2 * pi)
        else:
            while True:  # исключения мы еще не проходили, поэтому предположим, что будет введено именно число
                self.set_sides(int(input('Введите одно целое число больше 0: ')))
                if self.check_valid_sides(self.get_sides()[0]):
                    self.__radius = self.get_sides()[0] / (2 * pi)
                    break

    def get_square(self):
        from math import pi
        return pi * self.__radius ** 2

    def get_radius(self):
        return self.__radius


# ____________ПРОВЕРЯЕМ КРУГ__________________
print('Сразу вводим два отрицательных значения.')
print('Первое надо исправить, а на второе программа не должна обращать внимания')

circ1 = Circle([-100, -200], 'red', False)
print(f'Радиус: {circ1.get_radius()}')
print(f'Площадь круга: {circ1.get_square()}')
