from mammal import Mammal
class People(Mammal):
    def __init__(self, name, surname, gender, age):
        Mammal.__init__(self, age, gender)
        self.name = name
        self.surname = surname
