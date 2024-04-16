# The following function accepts an array of numbers and returns the sum, as long as a particular number doesn’t 
# bring the sum above 100. If adding a particular number will make the sum higher than 100, that number is ignored. 
# However, this function makes unnecessary recursive calls. Fix the code to eliminate the unnecessary recursion:
# def add_until_100(array):
#     if not array:
#         return 0
#     if array[0] + add_until_100(array[1:]) > 100:
#         return add_until_100(array[1:])
#     else:
#         return array[0] + add_until_100(array[1:])
    
def add_until_100(array):
    if not array:
        return 0
    
    remaining_array_sum = add_until_100(array[1:])
    if array[0] + remaining_array_sum > 100:
        return remaining_array_sum
    else:
        return array[0] + remaining_array_sum
    
print(add_until_100([15,20,35,40,55,260]))