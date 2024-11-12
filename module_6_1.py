# ________________Animals___________________________________
class Animal:
    alive = True
    fed = False
  
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    pass


# ________________Plants___________________________________
class Plant:
    edible = False
    name = ''


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    def __init__(self, name):
        self.name = name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
p2.edible = True

print(a1.name)
print(p1.name)
print()
print('Состояние животного ', a1.name, ' :', a1.alive)
print('Сытость животного ', a2.name, ' :', a2.fed)
print()
a1.eat(p1)
a2.eat(p2)
print('Состояние животного ', a1.name, ' :', a1.alive)
print('Сытость животного ', a2.name, ' :', a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
