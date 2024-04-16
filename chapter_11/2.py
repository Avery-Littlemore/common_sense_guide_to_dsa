# Use recursion to write a function that accepts an array of numbers and returns a new array containing just the even numbers.

def even_numbers_from(array):
    if not array:
        return []
    if array[0] % 2 == 0:
        return [array[0]] + even_numbers_from(array[1:])
    return even_numbers_from(array[1:])


print(even_numbers_from([1,2,3,4,5,6,7,8]))