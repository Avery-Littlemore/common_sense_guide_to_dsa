# This problem is known as the unique paths problem: Let’s say you have a grid of rows and columns. 
# Write a function that accepts a number of rows and a number of columns and calculates the number of 
# possible “shortest” paths from the upper-leftmost square to the lower-rightmost square. 

def number_of_shortest_unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return number_of_shortest_unique_paths(rows - 1, columns) + number_of_shortest_unique_paths(rows, columns - 1)

print(number_of_shortest_unique_paths(2, 1))
print(number_of_shortest_unique_paths(2, 2))
print(number_of_shortest_unique_paths(3, 2))
print(number_of_shortest_unique_paths(3, 3))
print(number_of_shortest_unique_paths(2, 4))


"""
2 x 1 => 1 path
2 x 2 => 2 paths
2 x 3 => 3 paths
3 x 3 => 6 paths
2 x 4 => 4 paths
"""

