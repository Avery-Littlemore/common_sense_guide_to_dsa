# You’re writing a function that accepts an array of numbers and computes the highest product of any two numbers in the array. 

# At first glance, this is easy, as we can just find the two greatest numbers and multiply them. However, our array can contain 
# negative numbers and look like this:
# [5, -10, -6, 9, 4]

# In this case, it’s actually the product of the two *lowest* numbers, -10 and -6 that yield the highest product of 60.

# We could use nested loops to multiply every possible pair of numbers, but this would take O(N^2) time. Your job is 
# to optimize the function so that it’s a speedy O(N).

def highest_product(array):
    highest_pos = float('-inf')
    second_highest_pos = float('-inf')
    lowest_neg = float('inf')
    second_lowest_neg = float('inf')

    for num in array:
        if num >= highest_pos:
            highest_pos, second_highest_pos = num, highest_pos
        elif num > second_highest_pos:
            second_highest_pos = num

        if num <= lowest_neg:
            lowest_neg, second_lowest_neg = num, lowest_neg
        elif num < second_lowest_neg:
            second_lowest_neg = num

    if highest_pos * second_highest_pos > lowest_neg * second_lowest_neg:
        return highest_pos * second_highest_pos
    else:
        return lowest_neg * second_lowest_neg

print(highest_product([5, -10, -6, 9, 4]))

print(highest_product([-5, -4, -3, 0, 3, 4])) # -> Greatest product: 20 (-5 * -4)
print(highest_product([-9, -2, -1, 2, 3, 7])) # -> Greatest product: 21 (3 * 7)
print(highest_product([-7, -4, -3, 0, 4, 6])) # -> Greatest product: 28 (-7 * -4)
print(highest_product([-6, -5, -1, 2, 3, 9])) # -> Greatest product: 30 (-6 * -5)
print(highest_product([-9, -4, -3, 0, 6, 7])) # -> Greatest product: 42 (6 * 7)