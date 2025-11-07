# # родитель, суперкласс
# class Car:
#     # инициализатор объектов
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def drive(self, location):
#         print(f"Car {self.model} is driving in {location}")

#     def test(self):
#         self.drive("Karakol")

# # дочерний, подкласс, потомок
# class Bus(Car):
#     def __init__(self, color, model, seats):
#         super().__init__(color, model)
#         self.seats = seats

#     def drive(self, location):
#         # super().drive(location)
#         print(f"Bus {self.model} is driving in {location}")

#     def test_bus(self):
#         print(f"Bus test {self.model}")


# class Truck(Car):
#     pass

# car_honda = Car("white", "Honda")
# bus_1 = Bus("green", "Isuzu", 40)
# print(bus_1.seats)
# print(bus_1.color)
# bus_1.drive("Bishkek")
# # bus_1.test_bus()
# truck_man = Truck("red", "Man")

# # Полиморфизм
# vehicles = [car_honda, bus_1, truck_man]
# for v in vehicles:
#     v.drive(location='Karakol')

# родитель, суперкласс
# Инкапсуляция 
class Car:
    # инициализатор объектов
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self._fined = False
        self.__spedd = 0

    def drive(self, location):
        print(f"Car {self.model} is driving in {location}, speed is {self.__spedd} and fine {self._fined}")

    def test(self):
        self.drive("Karakol")

    def get_speed(self):
        # геттер - для приватных методов
        return self.__spedd
    
    def set_speed(self, value):
        #  сеттер - заменить или дать 
         self.__spedd = value 
    def set_speed(self, value):
        if value <= 0:
            print('Max speed must be positive' )
            return
        self.__spedd= value



# дочерний, подкласс, потомок
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats = seats

    def drive(self, location):
        # super().drive(location)
        print(f"Bus {self.model} is driving in {location} and fine {self._fined}")

    def test_bus(self):
        print(f'Bus test {self.model}')


car_honda = Car("white", "Honda")
bus_1 = Bus("green", "Isuzu", 40)
print(bus_1.seats)
print(bus_1.color)
bus_1.drive("Bishkek")
print(car_honda.get_speed)