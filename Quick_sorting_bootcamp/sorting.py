def quick_sorting(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]

        return quick_sorting(left) + [pivot] + quick_sorting(right)


array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 10]
sorted_array = quick_sorting(array)
print(sorted_array)