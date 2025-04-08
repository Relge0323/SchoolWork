# Car class
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year
    
    def get_speed(self):
        return self.__speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
    def __str__(self):
        txtStr = "Car Info:\n" + \
                " Make:  " + self.__make + "\n" + \
                " Model: " + self.__model + "\n" + \
                " Year:  " + str(self.__year)
        return txtStr