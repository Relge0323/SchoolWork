def merge_sort(arr):
    if len(arr) <= 1:
        return arr      # base case: a list of 1 element is already sorted
    
    # step 1: Divide the list into two halves
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # step 2: Recursively sort both halves
    leftSorted = merge_sort(leftHalf)
    rightSorted = merge_sort(rightHalf)

    # Step 3: Merge the sorted halves
    return merge(leftSorted, rightSorted)


def merge(left, right):
    sortedList = []
    i = j = 0

    # Step 4: Compare the elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1
    
    # add any remaining elements from both halves
    sortedList.extend(left[i:])
    sortedList.extend(right[j:])

    return sortedList