"""
Author:
Date:
Filename: employee.py
"""

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    #Mutator methods
    def setName(self, name):
        self.__name = name

    def setNumber(self, number):
        self.__number = number
    
    #Accessor methods
    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shiftNumber, payRate):
        #call the superclass/parent class __init__ method
        Employee.__init__(self, name, number)
        self.__shiftNumber = shiftNumber
        self.__payRate = payRate

    #Mutator methods
    def setShiftNumber(self, shiftNumber):
        self.__shiftNumber = shiftNumber
    
    def setPayRate(self, payRate):
        self.__payRate = payRate

    #Accessor methods
    def getShiftNumber(self):
        return self.__shiftNumber
    
    def getPayRate(self):
        return self.__payRate
    
    def __str__(self):
        strText = str()
        strText += "Employee name: " + str(Employee.getName(self)) + \
                    "\n    ID Number: " + str(Employee.getNumber(self)) + \
                    "\n        Shift: " + str(self.__shiftNumber) + \
                    "\n   Hourly Pay: $" + str(self.__payRate)
        return strText