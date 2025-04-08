# write a function named remove that gets a string and an integer
# and returns the string without a letter in the index corresponding
# to the integer

def remove(a_string, number):
    firstSlice = a_string[:number]
    endSlice = a_string[number + 1:]

    return firstSlice + endSlice


print(remove('The best thing', 8))