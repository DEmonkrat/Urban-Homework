# __________________Figure_________________________
class Figure:
    SIDES_COUNT = 0

    def __init__(self, color, *sides, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled
        if not self.__is_valid_sides(*self.__sides):
            self.__sides = (1,) * self.SIDES_COUNT  # Если не прошли проверку сторон, то все длины строн 1
        if not self.__is_valid_color(*self.__color):
            self.__color = (255, 0, 0)  # Если не прошли проверку по цвету, то цвет КРАСНЫЙ

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
        # Вводим переменную sd_cnt для проверки Куба (у него передаем 1 стороуну вместо 12)
        if isinstance(self, Cube):
            sd_cnt = 1
        else:
            sd_cnt = self.SIDES_COUNT
        sides_bool = True
        for side in args:
            if (not isinstance(side, int)) or (side < 0) or (len(args) != sd_cnt):
                sides_bool = False
                break
        return sides_bool

    def get_sides(self):  # _________get_sides_____________
        return self.__sides

    def __len__(self):
        pass

    def set_sides(self, *new_sides):  # _________set_sides_____________
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            print(f'Стороные не удовлетворяют требованиям.')


# __________________Circle_________________________
class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, color, *sides, filled=False):
        from math import pi
        super().__init__(color, *sides, filled=filled)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        from math import pi
        return pi * self.__radius ** 2

    def get_radius(self):
        return self.__radius

    def set_sides(self, *new_sides):  # перегружаем метод, т.к. требуется пересчет радиуса
        from math import pi
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * pi)


# __________________Triangle_________________________
class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__trng_check()

    def get_square(self):
        sides = self.get_sides()
        # Используем формулу Герона для площади треугольника
        p = sum(sides) * 0.5
        return (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5

    def __trng_check(self):  # Служебная. Проверка возможности создания треугольника с такими сторонами
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        if (a + b) < c or (a + c) < b or (c + b) < a:
            print(f'Невозможно создать треугольник с такими стронами: {self.get_sides()}')
            self.set_sides(1, 1, 1)


# __________________Cube_________________________
class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, color, *sides, filled=False):
        super().__init__(color, *sides, filled=filled)
        self.__sides = sides * self.SIDES_COUNT

    def get_volume(self):
        return self.__sides[0] ** 3


print('____________ПРОВЕРЯЕМ КРУГ__________________')
print('Круг. Отрицательное значение сторон')
circ1 = Circle((1, 2, 3), -100)
print(f'Радиус: {circ1.get_radius():.2f}')
print(f'Площадь круга: {circ1.get_square():.2f}')
print(f'Цвет: {circ1.get_color()}')
print()
print('Круг.Сторон больше, чем надо')
circ2 = Circle((1, 2, 3), 100, 200)
print(f'Радиус: {circ2.get_radius():.2f}')
print(f'Площадь круга: {circ2.get_square():.2f}')
print(f'Цвет: {circ2.get_color()}')
print()
print('Круг.Передаем в длины строку')
circ3 = Circle((1, 2, 3), '100')
print(f'Радиус: {circ3.get_radius():.2f}')
print(f'Площадь круга: {circ3.get_square():.2f}')
print(f'Цвет: {circ3.get_color()}')
print()
print('Круг. Создаем правильный круг но неправильный цвет')
circ4 = Circle((1, 2, 300), 300)
print(f'Радиус: {circ4.get_radius():.2f}')
print(f'Площадь круга: {circ4.get_square():.2f}')
print(f'Цвет: {circ4.get_color()}')
print()
print('Круг.Присваиваем неправильные длины сторон')
circ4.set_sides(3, 4)
print(f'Радиус: {circ4.get_radius():.2f}')
print('Круг.Присваиваем правильные длины сторон')
circ4.set_sides(1)
print(f'Радиус: {circ4.get_radius():.2f}')
circ4.set_color(0, -1, 5)
print(f'Цвет: {circ4.get_color()}')
circ4.set_color(0, 200, 100)
print(f'Цвет: {circ4.get_color()}')

print()
print()
print('____________ПРОВЕРЯЕМ ТРЕУГОЛЬНИК__________________')
print('Треугольник. Неправильное кол-во сторон')
trng1 = Triangle((100, 200, 200), 5, 6, 7, 8)
print(trng1.get_sides())
print()
print('Треугольник. Невозможные длины сторон')
trng2 = Triangle((100, 200, 200), 5, 6, 20, )
print(trng2.get_sides())
print()
print('Треугольник. Все норм')
trng2 = Triangle((100, 200, 200), 5, 6, 7, filled=True)
print(trng2.get_sides())
print(f'Площадь треугольника: {trng2.get_square():.2f}')
print(f'Заливка: {trng2.filled}')
print()
print()
print('____________ПРОВЕРЯЕМ КУБ__________________')
print('Куб. Неправильное кол-во сторон')
cube1 = Cube((100, 200, 200), 1, 2, 3)
print('Стороны: ', cube1.get_sides())
print('Куб. Все норм')
cube2 = Cube((100, 200, 200), 3)
print('Стороны: ', cube2.get_sides())