class Hors:

    x_distance = 0
    sound = 'Frrr'

    def run(self,dx):
        self.x_distance += dx
        return self.x_distance

class Egle:

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        dy = self.y_distance + dy
        self.y_distance = dy

class Pegasus(Hors, Egle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Egle().sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
# print(Pegasus.mro())