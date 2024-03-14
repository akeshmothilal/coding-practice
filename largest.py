import  array as arr

def find_max(numbers):
    largest_element = numbers[0]
    i = 0
    while i<len(numbers):
        if numbers[i] > largest_element:
             largest_element = numbers[i]
        i = i+1

    return largest_element;




numbers = arr.array('i',[4,2,3,423,4,5])
print("larest element: ", end=" " ,)
print(find_max(numbers))

