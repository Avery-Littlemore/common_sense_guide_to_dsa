def group_sort(array): 
    hash_table = {}
    new_array = []
    
    for value in array:
        if value in hash_table:
            hash_table[value] += 1
        else:
            hash_table[value] = 1
    
    for key in hash_table: 
        count = hash_table[key] 
        for i in range(count):
            new_array.append(key) 
            
    return new_array