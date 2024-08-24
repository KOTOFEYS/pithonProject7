class Vehicle:

    __COLOR_VARIANTS = ['white', 'black', 'grey', 'red', 'yellow' ]

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель:{self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя:{self.__engine_power}'

    def get_color(self):
        return f'Цвет:{self.__color}'

    def get_owner(self):
        return f'Владелец:{self.owner}'

    def print_info(self):
        print(vehicle1.get_model())
        print(vehicle1.get_horsepower())
        print(vehicle1.get_color())
        print(vehicle1.get_owner())

    def set_color(self, new_color):
        for __color in self.__COLOR_VARIANTS:
            if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5
    owner = 'Vasyok'


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500 , 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('pink')

vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
