# The following function uses recursion to calculate the Nth number from a mathematical sequence known as the Golomb sequence. 
# It’s terribly inefficient, though! Use memoization to optimize it. 

def golomb(n, memo):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return 1 + memo[n]