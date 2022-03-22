"""Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence. 
The 0th number of the sequence is 0. The 1st number of the sequence is 1. To generate the next number of the sequence, we sum the previous two."""

def fib(n, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    print(cache)
    if n in cache: return cache[n]  
    if n <= 1: return n
    
    # Recursive Step
    cache[n] = fib(n-1) + fib(n-2)  # update cache and return
    return cache[n]

# Test Cases
print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025