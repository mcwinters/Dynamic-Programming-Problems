"""Write a function best_sum(target, numbers) that takes in a target and a list of numbers as arguments. 
The function should return a list containing the shortest combination of numbers that add up to exactly the target.
If there a tie for the shortest combination, you may return any one of the shortest."""

def bestSum(target, numbers, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]
    if target == 0: return []
    if target < 0: return None
    
    result = None 
    
    # Recursive Step
    for number in numbers:   # iterate through numbers
        remainder = target - number  # calculate remainder
        remainderResult = bestSum(remainder, numbers, cache)  # recursive call
        if remainderResult != None:  # if valid
            tempResult = remainderResult + [number]  # create temp and add new number
            if (result == None) or (len(tempResult) < len(result)):  # if we need to update result, update
                result = tempResult
    
    cache[target] = result
    return result

# Test Cases
print(bestSum(7, [2,3]))  # [3, 2, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))  # None
print(bestSum(8, [2, 3, 5]))  # [5, 3]
print(bestSum(300, [7, 14]))  # None
