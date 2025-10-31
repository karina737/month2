class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name=name
        self.birth_date=birth_date
        self.occupation=occupation
        self.higher_education=higher_education

    def introduce(self):
        print(f'Name is {self.name}, birthday: {self.birth_date}, occupation: {self.occupation}, highter education: {self.higher_education}')

person1=Person('Renata', '30.09.1996' , 'F/A', True )
person2=Person('Timur', '1.07. 1988', 'Captain', True)
person3=Person('Alla', '13.10.1999', 'Doctor', True)
person1.introduce()
person2.introduce()
person3.introduce()
