class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name=name
        self.birth_date=birth_date
        self.occupation=occupation
        self.higher_education=higher_education

    def introduce(self):
        print(f'Name is {self.name}, birthday: {self.birth_date}, occupation: {self.occupation}, highter education: {self.higher_education}')

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_main):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_main=group_main
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, я {self.group_main } Карины, я родился(лась) {self.birth_date}, у меня {self.higher_education} образование и я работаю {self.occupation}.')

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby=hobby
    def introduce(self):
        print(f'Привет,меня зовут {self.name},я родился(лась) {self.birth_date}, у меня {self.higher_education} образование и я {self.occupation}, так же увлекаюсь {self.hobby}.')

classmate1=Classmate('Улан', '15.05.1995','б/п','высшее','коллега')
classmate2=Classmate('Роман', '05.04.1997', 'командир ВС', 'высшее', 'коллега')
friend1=Friend('Ксения', '01.03.1999', 'предприниматель', 'высшее', 'косметикой')
friend2=Friend('Алла', '13.10.1999', 'доктор', 'высшее','спортом')
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

#доп задание 1
class Classmate:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print(f' Привет, меня зовут {self.name}, я твой одноклассник')

class Friend:
    def __init__(self, name):
        self.name=name

    def introduce(self):
        print(f'Привет, я твоя подруга, {self.name}')

class Person:
    def __init__(self, name):
        self.name=name

    def introduce(self):
        print(f'Привет, я твой знакомый {self.name}')

p1=Classmate('Артур')
p2=Friend('Аделя')
p3=Person('Азис')
people=[p1, p2, p3]

for person in people:
    person.introduce()

#доп задание 2
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name=name
        self.birth_date=birth_date
        self.occupation=occupation
        self.higher_education=higher_education

    def introduce(self):
        print(f'Name is {self.name}, birthday: {self.birth_date}, occupation: {self.occupation}, highter education: {self.higher_education}')

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby=hobby
    def introduce(self):
        print(f'Привет,меня зовут {self.name},я родился(лась) {self.birth_date}, у меня {self.higher_education} образование и я {self.occupation}, так же увлекаюсь {self.hobby}.')

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memoty=shared_memory

    def introduce(self):
        super().introduce()
        print(f'Наше классное воспоминание: когда мы {self.shared_memoty}')

bestfriend=BestFriend('Алла', '13.10.1999', 'доктор', 'высшее','спортом', 'вместе учились')
bestfriend.introduce()

