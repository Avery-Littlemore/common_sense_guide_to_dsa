# Given an array of positive numbers, write a function that returns the greatest product of any three numbers. 
# The approach of using three nested loops would clock in at O(N3), which is very slow. Use sorting to implement 
# the function in a way that it computes at O(N log N) speed.

def greatest_product_of_three(array):
    array.sort()
    return array[-1] * array[-2] * array[-3]

print(greatest_product_of_three([10,6,2,7,3]))
print(greatest_product_of_three([1,2,3,4,5,8,1,2,3]))