import array

def find_second_smallest(arr):
    smallest = arr[0]
    second_smallest = -3
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != second_smallest and arr[i] < smallest:
            second_smallest = arr[i]

    return second_smallest



arr =[40,34,3,43,4]
print(find_second_smallest(arr))



