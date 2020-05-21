from nothing import Nothing
from People import People
class Inhabitant(People):
    """this calss represents inhabitant object"""

    amount_members = 0
    def __init__(self, name = Nothing(), surname = Nothing(), gender = Nothing(), age = Nothing(), status = Nothing()):
        Inhabitant.amount_members += 1
        People.__init__(self, name, surname, gender, age)
        self.status = status
        
        if(status == 'S'):
            self.duty_degree = 2
        else:
            self.duty_degree = 0

    def __str__(self):
        return f"name - {self.name} surname - {self.surname} gender - {self.gender} age - {self.age}; status - {self.status}"

    def __del__(self):  # Деструктор класса
        Inhabitant.amount_members -= 1


