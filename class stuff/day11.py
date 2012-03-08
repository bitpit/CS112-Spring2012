#!/usr/bin/env python


class Student(object):    #if defining a class, you start it with a capital let.
    def __init__(self, name="Jane Doe"):
        self.name = name

    def say(self, message):  #self has reserved name; acces to all things 'self'
        print self.name+": "+message #self becomes whatever instance we call
                                     #the function on
    def say_to(self, other, message):
        self.say(message+", "+other.name+".")
    def printt(self):
        print self.name
    #pass

class Course(object):
    def __init__(self, name="Unknown"):
        self.name = name
        self.enrolled = []
    def enroll(self, student):
        self.enrolled.append(student)
    def printt(self):
        for student in self.enrolled:
            student.printt()


bob = Student("Bob")  #makes bob an instance of class Student
#bob.name = "Bob"    #gives the Student class an attribute "name" which is 'Bob'

fred = Student("Fred")
#fred.name = "Fred"

bob.say("hi fred.")
fred.say("go away, bob.")

razalghul = Student()
razalghul.say("fuck you mandingus.")

fred.say_to(bob, "fook a yu")

CS112 = Course("CS112")

CS112.enroll(fred)
CS112.enroll(bob)

CS112.printt()

bob2 = bob        #doesn't copy object in memory -> just copies assignment



#print bob
#print bob.name

