import math

class Figure:

    sides_count = 0

    def __init__(self, color, sides: int, filled=bool):
        self.__sides = ([sides] * self.sides_count)
        self.__color = list(color)
        self.filled = filled

    def __len__(self):
        return sum(self.__sides)

    def get_color(self,):
        return self.__color

    def get_sides(self,):
        return self.__sides

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]

    def set_sides(self, *args):
        new_sides = [*args]
        if self.__is_valid_sides(new_sides) == True:
            self.__sides = new_sides

    def __is_valid_color(self,r, g, b):
        if 0 < r < 255 and 0 < g < 255 and 0 < b < 255:
            return True
        else:
            False

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for i in new_sides:
                return True
        else:
            return False





class Circle(Figure):

    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color = color, sides = sides)
        self.r_circle = sides/(2 * math.pi)
        self.s_circle = math.pi * self.r_circle ** 2

    def get_radius(self):
        return self.r_circle

    def get_square(self):
           return self.s_circle

class Triangle(Figure):

    sides_count = 3

    def __init__(self,color, sides):
        super().__init__(color = color, sides = sides)
        self.p = 1/2 * (self.side_count * 3)     #где self.p = полупириметр треугольника
        self.s_triangle = math.sqrt(self.p*(3 * (self.p - self.sides_count)))

    def get_square(self):
        return self.s_triangle

class Cube(Figure):

    sides_count = 12

    def __init__(self, color,sides):
        super().__init__(color = color, sides = sides)
        self.__sides = sides

    def get_volume(self):
            return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())


print(circle1.get_radius())
print(circle1.get_square())
