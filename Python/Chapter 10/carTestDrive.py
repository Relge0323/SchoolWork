"""
Author: Silvia Preston
Date:
Filename:
Description:

"""

from car import Car

def main():
    myCar = Car("Maserati", "Grecale GT", 2025)
    print(myCar)

    carLists = []
    #if you have multiple cars, as the user to enter the 
    #number of cars and the info for each one
    numCars = int(input("How many cars do you have? >> "))
    for count in range(numCars):
        make = input("What is the make of this car? >> ")
        model = input("What is the model? >> ")
        year = int(input("What year is it? >> "))
        myOtherCars = Car(make, model, year)
        carLists.append(myOtherCars)
        print(myOtherCars)
    print()

    #call the accelerate method 5 times
    for count in range(5):
        myCar.accelerate()
        print(f'  Speed after accelerate... {myCar.get_speed()}')

    #call the brake method 5 times and
    #print the current speed after each 
    #brake
    for count in range(5):
        myCar.brake()
        print(f'  Speed after brake... {myCar.get_speed()}')

if __name__ == "__main__":
    main()