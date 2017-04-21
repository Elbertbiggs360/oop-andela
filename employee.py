from random import randint
from person import Person
from organization import Organization

class Employee(Person):
    def __init__(self, name, age, gender, title):
        Person.__init__(self, name, age, gender)
        self.id = randint(1,1000)
        self.title = title
    def message(self):
        return "Hi "+ self.name
        
    def work_for(self, organization):
        if isinstance(organization, Organization):
            self.organization = organization
        else:
            raise TypeError("Invalid organization")