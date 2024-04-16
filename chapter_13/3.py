# Write three different implementations of a function that finds the greatest number within an array.
# Write one function that is O(N^2), one that is O(N log N), and one that is O(N).

# O(N^2)
def greatest_number_1(array):
    if not array:
        return None
    for i in array:
        i_is_greatest_number = True
        for j in array:
            if j > i:
                i_is_greatest_number = False
        if i_is_greatest_number:
            return i

# O(N logN)
def greatest_number_2(array):
    if not array:
        return None
    array.sort()
    return array[-1]

# O(N)
def greatest_number_3(array):
    if not array:
        return None
    greatest_found = array[0]
    for i in range(1, len(array)+ 1):
        if array[i] > greatest_found:
            greatest_found = array[i]

    return greatest_found


print(greatest_number_1([3,1,2,35,7,8,0]))
print(greatest_number_2([3,1,2,35,7,8,0]))
# print(greatest_number_3([3,1,2,35,7,8,0]))