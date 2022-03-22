"""Write a function can_sum(target_sum, numbers) that takes in a target_sum and a list of numbers as arguments. 
The function should return a boolean indicating whether or not it is possible to generate the target_sum using numbers from the list. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."""

def canSum(target, numbers, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]
    if target == 0: return True
    if target < 0: return False
    
    # Receursive Step
    for number in numbers:  # iterate through numbers
        remainder = target - number  # calculate remainder
        remainderResult = canSum(remainder, numbers, cache)  # recursive call
        if remainderResult == True:  # if we have found a solution
            cache[target] = True  # update cache
            return True
        
    cache[target] = False  # update cache
    return False

# Test Cases
print(canSum(7, [2,3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum(300, [7, 14]))  # False