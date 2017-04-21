from employee import  Employee

class Employer(Employee):
    def __init__(self, name, age, gender, title):
        Employee.__init__(self, name, age, gender, title)
        self.subordinates = []

    def hire(self, employee):
        if isinstance(employee, Employee):
            self.subordinates.append(employee)
        else:
            raise TypeError
    def message(self):
        return "Welcome Employer"