###################### Poly : many , morphism : forms ######################
###################### we can achieve polymorphism through method overriding ######################

class Animal:
    def sound(self):
        print("General sound.........")

class Dog(Animal):
    def sound(self):
        print("Barking..........")

class Cat(Animal):
    def sound(self):
        print("Meowing............")


def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()
make_sound(d)
make_sound(c)