# ____________Animal___________________
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if (self._coords[2] + dz) < 0:
            print('It\'s too deep, i can\'t dive :(')
        else:
            self._coords[0] += dx * self.speed
            self._coords[1] += dy * self.speed
            self._coords[2] += dz * self.speed

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER <= 5:
            print('Sorry, i\'m peaceful :)')
        else:
            print('Be careful, i\'m attacking you 0_0')

    def speak(self):
        print(self.sound)


# ____________Bird___________________
class Bird(Animal):
    beak = True
    sound = 'tweat'

    def lay_eggs(self):
        from random import randint
        print(f'Here are(is) {randint(1, 4)} eggs for you')


# ____________AquaticAnimal___________________
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._coords[2] -= abs(dz) * self.speed // 2


# ____________PoisonousAnimal___________________
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
    sound = 'SSSsssSSSSSsssss'


# ____________Duckbill___________________
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'


b1 = Bird(5)
b1.attack()
b1.lay_eggs()
b1.move(1, 2, 3)
b1.get_coords()
b1.move(3, 4, -10)
b1.speak()
print(b1.__dict__)
print()

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()

db.lay_eggs()
