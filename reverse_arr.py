def reverse_array(arr):
    start_index = 0
    end_index = len(arr) - 1

    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

    return arr

my_array = [1, 2, 3, 4, 5]
print("Original array:", my_array)
print("Original array:", my_array)

print("Reversed array:", reverse_array(my_array))
print("Original array:", my_array)

