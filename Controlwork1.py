class Animal:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def make_sound(self):
        print('Какой то звук')

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age
    @name.setter
    def name(self, value):
        if not value[0].isupper():
         raise ValueError("Имя должно быть с большой буквы ")
        else:
         self.__name=value
    @age.setter
    def age(self, value):
       if value >= 20:
          raise ValueError("Животные столько не живут")
       else:
          self.__age=value

class Dog(Animal):
   def make_sound(self):
      print(f'Собака {self.name} делает Гав-Гав и ей {self.age} лет')

class Cat(Animal):
    def make_sound(self):
      print(f'Кошка {self.name} делает Мяу-Мяу и ей {self.age} лет')


dog=Dog('Шарик', 19)
cat=Cat('Мурка', 13)
dog.make_sound()
cat.make_sound()
dog.name='Тузик'
dog.age=2
cat.age=6
dog.make_sound()
cat.make_sound()




   


