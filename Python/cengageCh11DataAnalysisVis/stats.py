"""
File: stats.py

Defines functions to compute the mean, median, std, and mode
of a list of numbers.
"""

import math
import random

def mean(lst):
    """Returns the mean of a list of numbers."""
    return sum(lst) / len(lst)

def frequencies(lst):
    """Returns a dictionary keyed by the unique
    numbers and their frequencies in lst."""
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = {}
    for number in lst:
        freq = theDictionary.get(number, 0)
        theDictionary[number] = freq + 1
    return theDictionary

def mode(lst):
    """Returns the mode of a list of numbers."""
    theDictionary = frequencies(lst)
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result = key
            break
    return result

def modes(lst):
    """Returns the modes of a list of numbers."""
    # Obtain the set of unique numbers and their
    # frequencies, saving these associations in
    # a dictionary
    theDictionary = frequencies(lst)
    theMaximum = max(theDictionary.values())
    result = []
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result.append(key)
    return result

def median(lst):
    """Precondition: lst is non-empty.
    Returns the median of numbers in lst."""
    if len(lst) == 0: 
        raise RuntimeError("List must be non-empty. ")
    copy = list(lst)
    copy.sort()
    midpoint = len(lst) // 2
    if len(lst) % 2 == 1:
        return copy[midpoint]
    else:
        return mean([copy[midpoint - 1], copy[midpoint]])

def std(lst):
    """Precondition: lst is non-empty.
    Returns the standard deviation of the numbers in lst."""
    if len(lst) == 0: 
        raise RuntimeError("List must be non-empty. ")
    average = mean(lst)
    differences = map(lambda x: x - average, lst)
    squares = list(map(lambda x: x ** 2, differences))
    return math.sqrt(mean(squares))

def getRandomList(size, lower, upper, unique = False):
    """Returns a list of randomly generate numbers
    within the given bounds."""
    theList = []
    for count in range(size):
        number = random.randint(lower, upper)
        if unique:
            while number in theList:
                number = random.randint(lower, upper)
        theList.append(number)
    return theList

def main():
    """Tests the functions."""
    lst = input("Enter a list of numbers separated by space >> ")
    lst = lst.split()    
    lst = [int(x) for x in lst]

    print("List:", lst)
    print("Mode:", mode(lst))
    print("Median:", median(lst))
    print("Mean:", mean(lst))
    print("Standard deviation:", std(lst))    
    print("Frequencies:", frequencies(lst))
    lst.sort()
    print(f'Sorted list: {lst}\n')
       
    print("A list of 10 random numbers from 1 to 10:")
    lst = getRandomList(10, 1, 10)
    print(lst)
    
    print("\A list of 10 unique random numbers from 1 to 10:")
    lst = getRandomList(10, 1, 10, unique = True)
    print(lst)
    

# The entry point for program execution
if __name__ == "__main__":
    main()
     
    
        
