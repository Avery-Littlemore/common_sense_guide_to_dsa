# Here is a solution to the unique paths problem from an exercise in the previous chapter. Use memoization to improve its efficiency:

def unique_paths(rows, columns, memo):
    if rows == 1 or columns == 1:
        return 1
    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows, columns - 1, memo)
    return memo[(rows, columns)]

print(unique_paths(2, 1, {}))
print(unique_paths(2, 2, {}))
print(unique_paths(3, 2, {}))
print(unique_paths(3, 3, {}))
print(unique_paths(2, 4, {}))