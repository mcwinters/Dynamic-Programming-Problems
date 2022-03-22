def bestSum(target, numbers):
    # Create Table
    dp = [None for _ in range(target + 1)]
    dp[0] = []
    
    # Fill Table
    for i in range(target + 1):  # iterate through table
        if dp[i] != None:  # if valid
            for number in numbers:   # iterate through numbers
                newIndex = i + number 
                if newIndex <= target:  # avoid index error
                    if dp[newIndex] == None or len(dp[i]) + 1 < len(dp[newIndex]):  # if we need to update, update
                        dp[newIndex] = [number] + dp[i]
                        
    return dp[-1]
    
# Test Cases
print(bestSum(7, [2,3]))  # [3, 2, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))  # None
print(bestSum(8, [2, 3, 5]))  # [5, 3]
print(bestSum(300, [7, 14]))  # None