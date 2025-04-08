# The goal of the binary search is to find the index of the target elment in the array, not the value. thats why we return an index

def binary_search(arr, target):
    #left, right = 0, len(arr) - 1      this was kind of confusing to me but its the same as this
    left = 0
    right = len(arr) - 1


    while left <= right:
        mid = (left + right) // 2   # find the middle index

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

