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