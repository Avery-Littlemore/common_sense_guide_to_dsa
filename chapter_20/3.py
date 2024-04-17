# You’re working on some more stock-prediction software. The function you’re writing accepts an array of predicted 
# prices for a particular stock over the course of time.

# For example, look at this array of seven prices:
# [10, 7, 5, 8, 11, 2, 6]

# It predicts that a given stock will have these prices over the next seven days.
# (On Day 1, the stock will close at $10; on Day 2, the stock will close at $7; and so on.)

# Your function should calculate the greatest profit that could be made from a single “buy” transaction followed by a single “sell” transaction.

# In this example, the most money could be made if we bought the stock when it was worth $5 
# and sold it when it was worth $11. This yields a profit of $6 per share.

# Note that we could make even more money if we buy and sell multiple times, but for now, 
# this function focuses on the most profit that could be made from just *one* purchase followed by *one* sale.

# Now, we could use nested loops to find the profit of every possible buy-and-sell combination. 
# However, this would be O(N^2) and too slow for our hotshot trading platform. Your job is to optimize 
# the code so that the function clocks in at just O(N).

def greatest_profit(array):
    low_buy = array[0]
    high_sell = array[0]
    profit = 0

    for num in array:
        if num < low_buy:
            profit = high_sell - low_buy
            low_buy = num
        elif num > high_sell and num > low_buy:
            high_sell = num
            profit = high_sell - low_buy
    
    return profit

print(greatest_profit([10, 7, 5, 8, 11, 2, 11]))