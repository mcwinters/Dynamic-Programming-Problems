"""Write a function how_sum(target, numbers) that takes in a target and a list of numbers as arguments. 
The function should return a list containing any combination of elements that add up to exactly the target. 
If there is no combination that adds up to the target, then return None. If there are multiple combinations possible, you may return any single one. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."""

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
