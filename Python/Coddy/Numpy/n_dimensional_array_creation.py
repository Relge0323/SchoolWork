import numpy as np

def one_dimension_higher(lst):
    arr = np.array([lst])
    return arr

print(one_dimension_higher([1]))
print(one_dimension_higher([[2,2],[2,2]]))
print(one_dimension_higher([[[1],[1],[1],[1]]]))