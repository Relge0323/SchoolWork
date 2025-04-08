import numpy as np

def array_modifier(lst, value, index):
    ary = np.array(lst)

    firstSlice = ary[:index]
    endSlice = ary[index:]

    ary = np.append(firstSlice, value)
    ary = np.append(ary, endSlice)

    return ary