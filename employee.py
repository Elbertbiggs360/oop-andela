import math
from person import Person

class Employee(Person):
    def __init__(self, name, age, gender, title):
        #self.id = math.random()
        Person.__init__(self, name, age, gender)
        self.title = title
    def message(self):
        return "Welcome Employee"