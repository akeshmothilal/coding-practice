import array
def find_second_largest(arr):
    largest = arr[0]
    second_largest = -1
    for i in range(1,len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i]<largest and arr[i]>second_largest:
            second_largest = arr[i]


    return second_largest


arr=[32,4,56,7,8,45]
print("second largest element in array :", find_second_largest(arr))



#approach2

list = [1,3,4,5,66,5]

list.sort()


print(list)
print(list[-2])