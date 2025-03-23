###################### Single Inheritance : single parent child relationship ######################

# class Parent:
#     def speak(self):
#         print("Speaking bro..............")

# class Child(Parent):
#     def read(self):
#         print("Reading bro................")

# parent = Parent()
# parent.speak()

# child = Child()
# child.speak()
# child.read() 


###################### Multiple Inheritance : inherit from multiple parents ######################

# class flyer:
#     def fly(self):
#         print("i Can fly")

# class swimmer:
#     def swim(self):
#         print("I can Swim")


# class duck(flyer,swimmer):
#     pass

# d = duck()
# d.fly()
# d.swim()


###################### Multilevel inheritance : continues inheriance by level ######################

# class Living_being():
#     def breath(self):
#         print("Breathing.............")

# class Animal(Living_being):
#     def eat(self):
#         print("Eating.................")

# class Dog(Animal):
#     def bark(self):
#         print("Barking.................")

# d = Dog()
# d.breath()
# d.eat()
# d.bark()


###################### Hirarchical Inheritance ######################

class vehicle:
    def starting(self):
        print("Strting........")
    def stopping(self):
        print("Stoping..........")

class car(vehicle):
    pass

class bike(vehicle):
    pass

c = car()
b = bike()

c.starting()
c.stopping()
b.stopping()
b.starting()
