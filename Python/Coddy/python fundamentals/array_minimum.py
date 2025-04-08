def min(arr):
    min_num = arr[0]
    for i in arr:
        if i < min_num:
            min_num = i
    return min_num


print(min([-2,5,1,65]))