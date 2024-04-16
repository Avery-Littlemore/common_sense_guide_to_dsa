# The following function finds the missing number from an array of integers; that is, the array is expected to have all integers 
# from 0 up to the array’s length, but one is missing. As examples, the array [5, 2, 4, 1, 0] is missing the number 3, and the 
# array [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8. 

# Here’s an implementation that is O(N^2) (the clause if number not in array is itself already O(N), since the computer needs to 
# search the entire array to find number):

# def find_missing_number(array):
#     for number in range(len(array) + 1):
#         if number not in array:
#             return number
    
#     return None

# Use sorting to write a new implementation of this function that only takes O(N log N). (Some other implementations are even faster, 
# but we’re focusing on using sorting as a technique to make code faster.)

def find_missing_number(array):
    array.sort()
    for number in range(len(array) + 1):
        if array[number + 1] - number != 1 :
            return number + 1
    
    return None

print(find_missing_number([5, 2, 4, 1, 0]))
print(find_missing_number([9, 3, 2, 5, 6, 7, 1, 0, 4]))

# def find_missing_number(array):
#     array.sort()
#     for index, num in enumerate(array):
#         if num != index:
#             return index
        
#     return None