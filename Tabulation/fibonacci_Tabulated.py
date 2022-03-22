"""Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence. 
The 0th number of the sequence is 0. The 1st number of the sequence is 1. To generate the next number of the sequence, we sum the previous two."""

def fib(n):
    # Create Table
    dp = [None] * (n+1)  # initialize table full of None's
    dp[0], dp[1] = 0, 1  # input seed values
    
    # Fill Table
    for i in range(2, n+1):  # iterate through table
        dp[i] = dp[i-1] + dp[i-2]  # update table
        
    return dp[-1]

# Test Cases
print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025