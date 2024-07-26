#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array with total + 1 (which is more than max possible coins)
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    
    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != total + 1 else -1
