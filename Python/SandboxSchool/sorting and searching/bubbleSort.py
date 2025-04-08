def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        noSwap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                noSwap = False
        if noSwap:
            return




myList = [8, 6, 15, 22, 25, 5, 8, 4, 24, 14]


bubble_sort(myList)

print(myList)