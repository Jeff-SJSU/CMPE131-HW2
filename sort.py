
def sort_list(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    
    return arr

#print(sort_list([1, 3, 2, 7]))
#print(sort_list([3, 2, 4, 89]))
