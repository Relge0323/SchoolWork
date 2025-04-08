class Calculator:
    def __init__(self, value):
        self.__value = value
    

    def add(self, value):
        self.__value += value

    def subtract(self, value):
        self.__value -= value

    def multiply(self, value):
        self.__value *= value
    
    def divide(self, value):
        try:
            self.__value /= value
            return None

        except ZeroDivisionError:
            return 'You can\'t divide by zero!'

        
    def get_result(self):
        return self.__value