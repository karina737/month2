# родительский класс, суперкласс
class Car:
# инициализатор
    def __init__(self, color, model):
        self.color=color
        self.model=model

    def drive(self, location):
        print(f' Car {self.model} is driving in {location}')

    def test(self):
        self.drive("Karakol")

car_honda= Car(color = 'Red', model= 'Honda')
car_subaru=Car(color='green', model= 'Subaru')
car_subaru.drive('Bishkek')
print(car_honda)
print(car_subaru)
print(car_honda.color)
print(car_subaru.color)

# дочерний, подкласс, потомок
class Bus(Car):
    def __init__(self, color, model, seats):
        super().__init__(color, model)
        self.seats=seats

    def drive(self, location):
        print(f' Bus {self.model} is driving in {location}')
    
    
    def test_bus(self):
        print(f"Bus test {self.model}")

bus_1=Bus("green", "RR", 148)
print(bus_1.color)
bus_1.drive("Bishkek")
bus_1.test_bus()
print(bus_1.seats)