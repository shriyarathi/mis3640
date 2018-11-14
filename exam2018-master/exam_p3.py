class Employee:
    """
    the base class
    """
    nextIdNum = 0

    def __init__(self, name):
        self.name = name 
        self.idNum = Employee.nextIdNum
        Employee.nextIdNum += 1
    def get_id(self):
        return self.idNum

    def get_name(self):
        return self.name

    def weekly_pay(self, hours_worked):
        return 0
    
    #employee needs a special method that overloads one type of operators, test this in main()
 
    def __str__(self):
        return self.name



class Nonexempt_Employee(Employee):


    def __init__(self, name, hourly_rate):
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate
        

    # Overrides the superclass method.
    def weekly_pay(self, hours_worked):
        pass  # delete this line and replace with your code here

        # non exempt employees are paid an hourly rate, but if work more than 40 hours, the excess is time and a half
        # have a special attribute hourly_rate

        pay = 0 

        if hours_worked > 40:
            pay = 40 * self.hourly_rate + ((hours_worked - 40)* self.hourly_rate*1.5)       
        else:
            pay = self.hourly_rate * hours_worked
        
        return pay


class Exempt_Employee(Employee):
    # exempt employees get paid their salary no matter how many hours they work 
    # exempt employees make at least $23,660 a year or $455 per week
    # they have a special attribute called annual_salary
    
    def __init__(self, name, annual_salary):
        Employee.__init__(self, name)
        self.annual_salary = annual_salary
    def get_annualsalary(self):
        return self.annual_salary

    def weekly_pay(self, hours_worked):
        return self.annual_salary/52

class Manager(Exempt_Employee):
    # managers get paid an annual salary plus a bonus 
    # bonus is an attribite of manager 
    def __init__(self, name, annual_salary, bonus):
        Exempt_Employee.__init__(self, name, annual_salary)
        self.bonus = bonus
    def get_bonus(self):
        return self.bonus
    

   

def main():
    all_employees = []
    all_employees.append(Nonexempt_Employee("Aaron Wendell", 40.0))
    all_employees.append(Exempt_Employee("Alden Pexton", 60000.0))
    all_employees.append(Manager("Allison Fernandez", 94000.0, 50.0))
    
    

    for employee in all_employees:
        hours = int(input("Hours worked by " + str(employee) + ": "))   # this is testing the overidden __str__ function
        pay = employee.weekly_pay(hours)
        print("Salary: ", pay)


if __name__ == '__main__':
    main()
