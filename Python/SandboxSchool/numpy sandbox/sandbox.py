import math

def mean(lyst):
    if len(lyst) == 0:
        raise RuntimeError("error")
    return sum(lyst) / len(lyst)


def median(lyst):
    if len(lyst) == 0:
        raise RuntimeError("error")
    
    copy = list(lyst)
    copy.sort()

    midpoint = len(lyst) // 2   # why arent we getting len(copy)?

    if len(lyst) % 2 == 1:
        return copy[midpoint]
    else:
        return mean([copy[midpoint - 1], copy[midpoint]])
    

def frequencies(lyst):
    """return a dictionary of numbers and their frequenceis in lyst"""
    mySpellbook = {}
    for spell in lyst:
        count = mySpellbook.get(spell, 0)
        mySpellbook[spell] = count + 1
    return mySpellbook



def mode(lyst):
    if len(lyst) == 0:
        raise RuntimeError("Error")
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())

    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result = key
            break
    return result


def modes(lyst):
    if len(lyst) == 0:
        raise RuntimeError("error")
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    result = []

    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result.append(key)
    return result


def std(lyst):
    if len(lyst) == 0:
        raise RuntimeError("error")
    
    average = mean(lyst)
    differences = map(lambda x: x - average, lyst)
    squares = list(map(lambda x: x**2, differences))
    return math.sqrt(mean(squares))