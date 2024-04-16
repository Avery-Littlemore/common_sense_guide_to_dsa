# Use recursion to write a function that accepts an array of strings and returns the total number of characters across all the strings. 
# For example, if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there are ten characters in total.

def total_num_of_chars(array):
    if not array:
        return 0
    if len(array) == 1:
        return len(set(array[0]))
    
    unique_from_first_two_elements = ''.join(set(array[0] + array[1]))
    if len(array) == 2:
        return len(set(unique_from_first_two_elements))
    
    return total_num_of_chars([unique_from_first_two_elements] + array[2:])

print(total_num_of_chars(["ab", "c", "def", "ghij"]))
print(total_num_of_chars(["ab", "c", "def", "ghijaaaaabbbbcccc"]))