'''Problem:

You are tasked with creating a class hierarchy for a simple Employee Management System. The base class will represent a general Employee, and the derived classes will represent different types of employees such as Manager and Developer.

Requirements:

Employee Class:

Define an Employee class that has the following attributes:

name: a string representing the employee's name.

age: an integer representing the employee's age.

salary: a float representing the employee's salary.

Define an __init__ method to initialize these attributes.

Implement a method get_details that returns a string with the employee's name, age, and salary.

Manager Class (inherits from Employee):

The Manager class should have an additional attribute department (a string representing the department the manager is in charge of).

Override the __init__ method using super() to call the Employee class's initializer.

Override the get_details method to also include the department information.

Developer Class (inherits from Employee):

The Developer class should have an additional attribute programming_language (a string representing the language they specialize in).

Override the __init__ method using super() to call the Employee class's initializer.

Override the get_details method to also include the programming language.
    

Sample Output:
employee = Employee("John", 30, 50000)
print(employee.get_details())  
# Output: Name: John, Age: 30, Salary: 50000

manager = Manager("Alice", 40, 80000, "HR")
print(manager.get_details())  
# Output: Name: Alice, Age: 40, Salary: 80000, Department: HR

developer = Developer("Bob", 25, 60000, "Python")
print(developer.get_details())  
# Output: Name: Bob, Age: 25, Salary: 60000, Programming Language: Python

Hint:

You’ll need to use super() to call the parent class's constructor (__init__) 
and initialize attributes in the derived classes properly.'''


class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        return f"Name : {self.name},Age : {self.age},Salary : {self.salary}"

class Manager(Employee):
    def __init__(self,name,age,salary,department_in_charge):
        self.department_in_charge = department_in_charge
        super().__init__(name,age,salary)

    def get_details(self):
        return f"Name : {self.name}, Age : {self.age}, Salary : {self.salary}, Department : {self.department_in_charge}"


class Developer(Employee):
    def __init__(self,programming_language,name,age,salary):
        self.programming_language = programming_language
        super().__init__(name,age,salary)
        

    def get_details(self):
        return f"Name : {self.name},Age : {self.age},Salary : {self.salary},Programming Language : {self.programming_language}"
    


employee = Employee("John", 30, 50000)
print(employee.get_details())  
# Output: Name: John, Age: 30, Salary: 50000

manager = Manager("Alice", 40, 80000, "HR")
print(manager.get_details())  
# Output: Name: Alice, Age: 40, Salary: 80000, Department: HR

developer = Developer("Bob", 25, 60000, "Python")
print(developer.get_details())  
# Output: Name: Bob, Age: 25, Salary: 60000, Programming Language: Python