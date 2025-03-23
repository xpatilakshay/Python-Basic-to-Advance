############## Super : Reference variable refers to parent class object ######################

# class Student:
#     def __init__(self,name):
#         self.name = name

#     def display(self):
#         print(f"my name is :  {self.name}")

# class Employee(Student):
#     def __init__(self,name,emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id

#     def display(self):
#         super().display()
#         print(f"Empleyee id : {self.emp_id}")
    
# s = Employee("Akshay",123)
# s.display()
        

############## Another example ##############

class vehicle:
    def __init__(self,carname):
        self.carname = carname

    def display(self):
        print(f"Car is {self.carname}")

class Car(vehicle):
    def __init__(self, carname,model):
        super().__init__(carname)
        self.model = model

    def display(self):
        super().display()
        print(f"Model is of {self.model}")

c = Car("Thar",2024)
c.display()
