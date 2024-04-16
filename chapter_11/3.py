# A particular numerical sequence is known as triangular numbers. The pattern begins as 1, 3, 6, 10, 15, 21, and continues onward. 
# To calculate the next number in the sequence, we add the previous number from the sequence plus N, where N corresponds to the 
# place in the sequence where the number lies. For example, the seventh number in the sequence is 28, since it’s the seventh number
# in the pattern, so we add the number 7 plus 21 (the previous number in the sequence). Write a function that accepts a number for
# N and returns the correct number from the series; that is, if the function was passed the number 7, the function would return 28.

def triangle(n):
    if n == 1:
        return 1
    return n + triangle(n - 1)

print(triangle(1)) # 1
print(triangle(2)) # 3
print(triangle(3)) # 6
print(triangle(4)) # 10
print(triangle(5)) # 15
print(triangle(6)) # 21
print(triangle(7)) # 28
