from employer import Employer
from employee import Employee
from organization import Organization

def main():
    employer = Employer('Victa Kironde', 25, 'male', 'LFA')
    organization = Organization('Andela', 'www.andela.com')
    employer.work_for(organization)
    #add subordinates
    employee = Employee('Bruce Bigirwenkya', 22, 'male', 'Fellow');
    employer.hire(employee)
    employer.hire(Employee('Daniel', 22, 'male', 'Developer'))
    employer.hire(Employee('Joshua', 18, 'male', 'Fellow'))
    employer.hire(Employee('Martina', 19, 'female', 'fellow'))
    employer.hire(Employee('Joshua', 20, 'male', 'Supervisor'))
    
    print("\n_____________________")
    print("Organization")
    print("---XXX---")
    print("Name: "+ employer.organization.name)
    print("Address: " + employer.organization.web_address)
    print("\n_____________________")
    print ("Details of employer:" )
    print("---XXX---")
    print ("Name: "+ employer.name)
    print ("Age: "+ str(employer.age))
    print ("Gender: "+ employer.gender)
    print ("Title: "+ employer.title)
    print ("Number of subordinates:"+ str(len(employer.subordinates)))
    print("\n_____________________")
    print ("Show polymorphism:")
    print("---XXX---")
    print ("Message for employee:"+employee.message())
    print ("Message for employer:"+employer.message())

if __name__ == "__main__":
    main()
