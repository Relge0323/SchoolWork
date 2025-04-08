import math
def mean(lyst):
    """Precondition: lyst is non-empty.
    Returns the arithmetic mean of numbers in lyst."""
    if len(lyst) == 0:
        raise RuntimeError("list must be non-empty.")
    return sum(lyst) / len(lyst)


def median(lyst):
    """Precondition: lyst is non-empty.
    Returns the median of numbers in lyst."""
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty.")
    copy = list(lyst)
    copy.sort()

    midpoint = len(lyst) // 2
    if len(lyst) % 2 == 1:
        return copy[midpoint]
    else:
        return  (copy[midpoint -1] + copy[midpoint]) / 2

def frequencies(lyst):
    """Returns a dictionary of numbers and their frequencies in lyst."""
    theDictionary = {}
    for number in lyst:
        count = theDictionary.get(number, 0)
        theDictionary[number] = count + 1
    return theDictionary

def mode(lyst):
    """Preconditoin: lyst is non-empty.
    Returns the mode of the numbers in lyst."""
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty")
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result = key
            break
    return result

def modes(lyst):
    """Precondition: lyst is non-empty
    Returns a list of the modes of the numbers in lyst."""
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty")
    theDictionary = frequencies(lyst)
    theMaximum = max(theDictionary.values())
    result = []
    for key in theDictionary:
        if theDictionary[key] == theMaximum:
            result.append(key)
    return result


def std(lyst):
    """Precondition: lyst is non-empty.
    Returns the standard deviation of the numbers in lyst."""
    if len(lyst) == 0:
        raise RuntimeError("List must be non-empty")
    # Step 1
    average = mean(lyst)
    # Step 2
    differences = map(lambda x: x - average, lyst)
    # Step 3
    squares = list(map(lambda x: x ** 2, differences))
    # Step 4 and 5
    return math.sqrt(mean(squares))

