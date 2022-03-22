"""Write a function how_sum(target_sum, numbers) that takes in a target_sum and a list of numbers as arguments. 
The function should return a list containing any combination of elements that add up to exactly the target_sum. 
If there is no combination that adds up to the target_sum, then return None. If there are multiple combinations possible, you may return any single one. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."""

def howSum(target, numbers):
    # Create Table
    dp = [None for _ in range(target + 1)]
    dp[0] = []
    
    # Fill Table
    for i in range(target + 1):  # iterate through table
        if dp[i] != None:  # check if current index is valid
            for number in numbers:  # iterate through numbers
                if i + number <= target:  # avoid index error
                    dp[i+number] = dp[i] + [number]  # update table
                    
    return dp[-1]
    
# Test Cases
print(howSum(7, [2,3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None