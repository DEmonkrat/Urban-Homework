# ________________Animals___________________________________
class Animal:
    alive = True
    fed = False
  
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print('Это что-то непонятное. Я это есть не буду !!!!')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass

# ________________Plants___________________________________
class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


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
a2.eat('Жаркое')
print('Состояние животного ', a1.name, ' :', a1.alive)
print('Сытость животного ', a2.name, ' :', a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
