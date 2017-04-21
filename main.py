from employer import Employer
from employee import Employee

def main():
    employer = Employer('Victa Kironde', 25, 'male', 'LFA')
    #add subordinates
    employee = Employee('Bruce Bigirwenkya', 22, 'male', 'Fellow');
    employer.hire(employee)
    employer.hire(Employee('Daniel', 22, 'male', 'Developer'))
    employer.hire(Employee('Joshua', 18, 'male', 'Fellow'))
    employer.hire(Employee('Martina', 19, 'female', 'fellow'))
    employer.hire(Employee('Joshua', 20, 'male', 'Supervisor'))
    print ("Details of employer:" )
    print("---XXX---")
    print ("Name: "+ employer.name)
    print ("Age: "+ str(employer.age))
    print ("Gender: "+ employer.gender)
    print ("Title: "+ employer.title)
    print ("Number of subordinates:"+ str(len(employer.subordinates)))
    print("---XXX---")
    print ("Show polymorphism:")
    print ("Message for employee:"+employee.message())
    print ("Message for employer:"+employer.message())

if __name__ == "__main__":
    main()
