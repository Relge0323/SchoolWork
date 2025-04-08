# selection sort

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        print(arr)
        print("inside the i loop")
        print(f"i is currently = {i}")
        min_index = i
        print(f"min_index inside the i loop is = {min_index}")

        for j in range(i + 1, n):
            print(f"j = {j}")
            print(f"if arr[{j}] < arr[{min_index}]:")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"{min_index} = {j}")

        print(f"swap occuring: arr[{i}], arr[{min_index}] = arr[{min_index}], arr[{i}]")
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr





nums1 = [20, 63, 85, 1, 89, 97, 27, 37, 35, 75]


print(selection_sort(nums1))