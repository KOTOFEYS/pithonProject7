class Animal:
    alive = True    # живой
    fed = False     # накормленный

class Plant:
    edible = False  # сытость

class Mammal(Animal):
    fed = True
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print(f'{self.name} съел {food.name}')

class Predator(Animal):
    alive = False
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print(f'{self.name} не стал есть {food.name}"')


class Flower(Plant):
    def __init__(self,name):
         self.name = name

class Fruit(Plant):
    def __init__(self, name):
        self.name = name



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)