##################### GLOBAL VARIABLE ####################

# a = "Akshay Patil" #Global Variable
# print(a)

##################### LOCAL VARIABLE ####################

# def car():
#     b = "BMW" #Local Variable
#     global a #To access global variable
#     a = "Thar"
#     print(b)
#     print(a)
# print(a)
# car()
# print(a)

##################### NONLOCAL VARIABLE ####################

# def car():
#     a = "BMW"
#     def bike():
#         nonlocala = "Honda" #Nonlocal variable
#         print(a)
#     bike()
#     print(a)
# car()

##################### INSTANCE VARIABLE AND CLASS VARIABLE ####################

class student:
    college = "KBP College Vashi"  #class variable
    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age

s1 = student("Akshay",20)
print(s1.name,s1.age)

s1 = student("Rohan",13)
print(s1.name,s1.age)

print(student.college)


