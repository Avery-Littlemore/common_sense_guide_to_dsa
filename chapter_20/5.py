# You’re creating software that analyzes the data of body temperature readings taken from hundreds of human beings. 
# These readings are taken from both healthy and sick people and range from 95 to 105 degrees Fahrenheit.

# Here’s a sample array of temperature readings:
# [98, 99, 95, 105, 104, 98, 101, 99, 100, 97]

# You are to write a function that sorts these readings from lowest to highest.

# If you used a classic sorting algorithm such as Quicksort, this would take O(N log N). *However, in this case, it’s 
# possible to write a faster sorting algorithm.*

# Yes, that’s right. Even though you’ve learned that the fastest sorts are O(N log N), this case is different. Why? 
# In this case, there’s a *limited number of possibilities* of what the readings will be. In such a case, we can sort 
# these values in O(N). It may be N multiplied by a constant, but that’s still considered O(N).

def sort_temps(array):
    hash_table = {}
    
    for temperature in array:
        if temperature in hash_table:
            hash_table[temperature] += 1
        else:
            hash_table[temperature] = 1
        
    sorted_temperatures = []
    temperature = 95

    while temperature <= 105:
        if temperature in hash_table:
            for i in range(hash_table[temperature]):
                sorted_temperatures.append(temperature)
            
        temperature += 1
                
    return sorted_temperatures

print(sort_temps([98, 99, 95, 105, 104, 98, 101, 99, 100, 97]))

