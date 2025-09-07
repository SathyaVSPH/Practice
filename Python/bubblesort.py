
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        idx = 0
        while idx < n - 1:
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            idx += 1
    return arr

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        idx = 0
        while idx < n - 1 - i:
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
            idx += 1
        if not swapped:
            break
    return arr

arr = [7, 11, 9, 12, 3]
print(bubble_sort(arr))