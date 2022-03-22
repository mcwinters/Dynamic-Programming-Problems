def howSum(target, numbers, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]
    if target == 0: return []
    if target < 0: return None
    
    # Recursive Step
    for number in numbers:  # iterate through numbers
        remainder = target - number  # calculate remainder
        remainderResult = howSum(remainder, numbers, cache)  # recursive call
        if remainderResult != None:  # if we have our answer
            cache[target] = remainderResult + [number]  # update cache and return
            return cache[target] 
    
    cache[target] = None
    return None

# Test Cases
print(howSum(7, [2,3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None