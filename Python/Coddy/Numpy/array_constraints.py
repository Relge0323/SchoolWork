import numpy as np
def array_modifier(lst, value, index):
    # convert the list to an array
    arr = np.array(lst)

    #string slicing
    start = arr[:index]
    end = arr[index:]

    start = np.append(start,value)
    start = np.append(start,end)
    return start

    

print(array_modifier([1,2,3],10,2))

