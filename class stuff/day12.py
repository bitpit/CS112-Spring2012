#!/usr/bin/env python

#object is grouping of atributes and functions which act pon de atributes
#refering to an object is an instance of a class

class Animal(object):
    def __init__(self, name):
        self.name = name
        pass

    def can_eat(self, food):
        pass

    def eat(self, food):
        pass

    def speak(self):  #<- abstract class- don't know what an animal speaks like
        pass

    def die(self):
        print self.name, "lived a good life, but passed."

    def __str__(self):
        return self.__class__.__name__+ ": " + self.name


class Dog(Animal):
    def can_eat(self, food):
        return True

    def eat(self, food):
        print self.name, "gobbles", food

    def speak(self):
        print self.name+" woof!"

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, "Mrs. "+name)
    
    def can_eat(self, food):
        return food.lower() == 'fish'
    
    def eat(self, food):
        print self.name, "sniffs", food
    
    def speak(self):
        print self.name, "walks away."

dog = Dog("Rover")
cat = Cat("Pretty")

print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance(cat, Cat)
print isinstance(cat, Dog)

print cat
