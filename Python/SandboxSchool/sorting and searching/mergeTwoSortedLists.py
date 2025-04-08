# write a function named merge that gets two sorted arrays of integers and returns a merged array of them sorted.
# use recursion

# without recursion
def merge(a1, a2):
    merged_list = a1 + a2
    merged_list.sort()
    print(merged_list)






def merge_recursively(a1, a2):
    if not a1:
        return a2
    if not a2:
        return a1
    
    if a1[0] < a2[0]:
        return [a1[0]] + merge_recursively(a1[1:], a2)
    else:
        return [a2[0]] + merge_recursively(a1, a2[1:])
    

    






array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

print(merge_recursively(array1, array2))