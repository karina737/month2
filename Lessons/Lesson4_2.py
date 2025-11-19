# # Инкапсуляция 
# class Car:
#     # инициализатор объектов
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#         self._fined = False
#         self.__spedd = 0

#     def drive(self, location):
#         print(f"Car {self.model} is driving in {location}, speed is {self.__spedd} and fine {self._fined}")

#     def test(self):
#         self.drive("Karakol")

#     # def get_speed(self):
#     #     # геттер - для приватных методов
#     #     return self.__spedd
    
#     # def set_speed(self, value):
#     #     #  сеттер - заменить или дать 
#     #      self.__spedd = value 
#     @property #- геттеро
#     def fined(self):
#         return self._fined
#     @fined.setter
#     def fined(self,val):
#         self._fined=val
#         if type(val) != bool:
#             raise TypeError('Fined must be booled')

#     def set_speed(self, value):
#         if value <= 0:
#             # print('Max speed must be positive' )
#             raise ValueError('Max speed must be positive' )
            
#         self.__spedd= value



# # дочерний, подкласс, потомок
# class Bus(Car):
#     def __init__(self, color, model, seats):
#         super().__init__(color, model)
#         self.seats = seats

#     def drive(self, location):
#         # super().drive(location)
#         print(f"Bus {self.model} is driving in {location} and fine {self._fined}")

#     def test_bus(self):
#         print(f'Bus test {self.model}')


# car_honda = Car("white", "Honda")
# bus_1 = Bus("green", "Isuzu", 40)
# print(bus_1.seats)
# print(bus_1.color)
# bus_1.drive("Bishkek")

# Абстракция
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print('Гав-Гав')

# puppy= Dog()
# puppy.make_sound()


class Car:
    cars_total=0
    def __init__(self, model, color):
        self.color=color
        self.model=model
        Car.cars_total+=1
    @staticmethod
    def validate_speed(speed):
        if speed<0:
            raise ValueError
        return True
        
    @classmethod
    def create(cls, color, model, speed):
        if Car.validate_speed(speed):
         new_car=Car(color, model, speed)
        return new_car
    @classmethod
    def get_car_total(cls):
        return cls.cars_total

    
car_mazda=Car.create('red', 'Mazda')
car_1=Car.create('white', 'Honda')
print(car_mazda.color)
print(Car.cars_total)

    
