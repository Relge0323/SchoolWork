"""

Author: Silvia Preston
File: student.py
Description: 

"""

class Student:
    """ This class represents a student."""
    #Constructor (or initializer) method
    #self is a must in all methods in a class
    def __init__(self):
        """ Initialize a default name and age for a 
        student. Attributes are private (__)"""
        self.__name = ''
        self.__age = 5
    
    #mutator
    def setName(self, name):
        """ This sets the name of the student."""
        self.__name = name
    
    #accessor
    def getName(self):
        """ Return the name of the student."""
        return self.__name
    
    #mutator
    def setAge(self, age):
        """ This sets the age of the student."""
        self.__age = age
    
    #accessor
    def getAge(self):
        """ Return the age of the student."""
        return self.__age

    #str method is needed in all Python classes
    #to print a string representation of the object
    def __str__(self):
        """ Returns the string representation of the student object"""
        return "Name: " + self.__name + "\n" + \
                "Age: " + str(self.__age)
