# def reverse(array):
#     new_array = []
#     for value in array:
#         new_array.insert(0, value)
        
#     return new_array

# Create a new function to reverse an array that takes up just O(1) extra space.

def reverse(array):
    current_index = 0
    while current_index < len(array) // 2:
        array[current_index], array[-current_index - 1] = array[-current_index - 1], array[current_index]
        current_index += 1

    return array


print(reverse([1,2,99,4,5]))
print(reverse([3,2,1,6,5,4]))