class Car:
# инициализатор
    def __init__(self, color, model):
        self.color=color
        self.model=model

    def drive(self, location):
        print(f' Car {self.model} is driving in {location}')
if __name__=='__main__':

 car_honda= Car(color = 'Red', model= 'Honda')
 car_subaru=Car(color='green', model= 'Subaru')
 car_subaru.drive('Bishkek')
 print(car_honda)
 print(car_subaru)
 print(car_honda.color)
 print(car_subaru.color)