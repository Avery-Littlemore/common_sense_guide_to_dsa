# You’re writing a function that accepts an array of unsorted integers and returns the length of the *longest 
# consecutive sequence* among them. The sequence is formed by integers that increase by 1. For example, have a look at this array:
# [10, 5, 12, 3, 55, 30, 4, 11, 2]

# The longest consecutive sequence is 2-3-4-5. These four integers form an increasing sequence because each integer is one greater
# than the previous one. While there’s also a sequence of 10-11-12, it’s only a sequence of three integers. In this case, the
# function should return 4, since that’s the length of the *longest* consecutive sequence that can be formed from this array.

# Here’s one more example:
# [19, 13, 15, 12, 18, 14, 17, 11]
# This array’s longest sequence is 11-12-13-14-15, so the function would return 5. 

# If we sorted the array, we can then traverse the array just once to find the longest consecutive sequence. However, the sorting 
# itself would take O(N log N). Your job is to optimize the function so that it takes O(N) time.

def longest_consecutive_seq(array):
    hash_table = {}
    max_seq = 0

    for num in array:
        pos_counter = 1
        neg_counter = 1
        hash_table[num] = True
        while hash_table.get(num + pos_counter):
            pos_counter += 1
            
        while hash_table.get(num - neg_counter):
            neg_counter += 1

        if pos_counter + neg_counter - 1 > max_seq:
            max_seq = pos_counter + neg_counter - 1

    return max_seq

print(longest_consecutive_seq([10, 5, 12, 3, 55, 30, 4, 11, 2])) # 4
print(longest_consecutive_seq([19, 13, 15, 12, 18, 14, 17, 11])) # 5
print(longest_consecutive_seq([6, 5, 4, 3, 2, 1])) # 6

def longest_sequence_length(array): 
    hash_table = {}
    greatest_sequence_length = 0
    
    for number in array:
        hash_table[number] = True
    
    for number in array:
        if not hash_table.get(number - 1):
            current_sequence_length = 1
            current_number = number
            
            while hash_table.get(current_number + 1):
                current_number += 1
                current_sequence_length += 1
                
                if current_sequence_length > greatest_sequence_length:
                    greatest_sequence_length = current_sequence_length
                    
    return greatest_sequence_length