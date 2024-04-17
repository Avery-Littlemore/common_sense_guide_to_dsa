# You’re writing a function that accepts an array of distinct integers from 0, 1, 2, 3...up to N. 
# However, the array will be missing one integer, and your function is to *return the missing one*.

# For example, this array has all the integers from 0 to 6 but is missing the 4:
# [2, 3, 0, 6, 1, 5]
# Therefore, the function should return 4. 

# The next example has all the integers from 0 to 9 but is missing the 1:
# [8, 2, 3, 9, 4, 7, 5, 0, 6]
# In this case, the function should return the 1.

# Using a nested-loops approach would take up to O(N^2). Your job is to optimize the code so that it has a runtime of O(N).

def get_missing_int(array):
    for num in range(min(array), max(array) + 1):
        if num not in array:
            return num
    
    return None
    
    # assumes array always starts from 0
    # for num in range(len(array)):
    #     if num not in array:
    #         return num
    
    # return None

print(get_missing_int([2, 3, 0, 6, 1, 5]))
print(get_missing_int([8, 2, 3, 9, 4, 7, 5, 0, 6]))
print(get_missing_int([1, 2, 3, 4, 5, 6])) # missing 0: sum = 21
print(get_missing_int([0, 2, 3, 4, 5, 6])) # missing 1: sum = 20
print(get_missing_int([0, 1, 3, 4, 5, 6])) # missing 2: sum = 19
print(get_missing_int([0, 1, 2, 4, 5, 6])) # missing 3: sum = 18
print(get_missing_int([0, 1, 2, 3, 5, 6])) # missing 4: sum = 17
print(get_missing_int([0, 1, 2, 3, 4, 6])) # missing 5: sum = 16