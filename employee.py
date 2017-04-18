import math
from person import Person

class Employee(Person):
    def __init__(self, title):
        self.id = math.random()
        self.title = title
    
    def work(self, assignment):
        move()
        communicate()
