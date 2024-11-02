class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def go_to(self, new_floor):
        if (new_floor < 1) | (new_floor > self.number_of_floors):
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(f'{i} этаж')


dom = House('ЖК Белая дача', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

print(dom.__str__())
print(dom.__len__())
print(h1.__str__())
print(h1.__len__())
print(h2.__str__())
print(h2.__len__())
