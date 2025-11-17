class Person:
    def __init__(self, name, birth_date, occupation,higher_education ):
        self.name=name
        self.birth_date=birth_date
        self.__occupation = occupation
        self.__higher_education= higher_education
        self.set_higher_education(higher_education)

    def introduce(self):
        print(f'Name is {self.name}, birthday: {self.birth_date}, occupation: {self.__occupation}, highter education: {self.__higher_education}')

    def get_occupation(self):
        return self.__occupation
    def get_higher_education(self):
        return self.__higher_education
    
    def set_higher_education(self, value):
        if value == True:
         self.__higher_education ='высшее'
        else:
         self.__higher_education = 'не законченное' 
         

class Classmate(Person):
    def __init__(self, name, birth_date, occupation,higher_education, group_main):
        super().__init__(name, birth_date ,occupation, higher_education)
        self.group_main=group_main
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я {self.group_main } Карины, я родился(лась) {self.birth_date}, у меня {self.get_higher_education()} образование и я увлекаюсь {self.get_occupation()}.')

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby=hobby
    def introduce(self):
        print(f'Привет,меня зовут {self.name},я родился(лась) {self.birth_date}, у меня {self.get_higher_education()} образование и я {self.get_occupation()}, так же увлекаюсь {self.hobby}.')

classmate1=Classmate('Улан', '15.05.1995','теннисом', False, 'коллега')
classmate2=Classmate('Роман', '05.04.1997', 'шахматами', True , 'коллега')
friend1=Friend('Ксения', '01.03.1999', 'предприниматель', True, 'косметикой')
friend2=Friend('Алла', '13.10.1999', 'доктор',True,'спортом')
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()




