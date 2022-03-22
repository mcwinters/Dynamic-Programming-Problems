"""Write a function can_sum(target_sum, numbers) that takes in a target_sum and a list of numbers as arguments. 
The function should return a boolean indicating whether or not it is possible to generate the target_sum using numbers from the list. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."""

def canSum(target, numbers):
    # Create Table
    dp = [False] * (target+1)
    dp[0] = True
    
    # Fill Table
    for i in range(target + 1):  # iterate through table
        if dp[i] == True:  # if current number is valid
            for number in numbers:  # iterate through numbers
                if i + number <= target:  # avoid index error
                    dp[i+number] = True  # update table
    
    return dp[-1]
    
# Test Cases
print(canSum(7, [2,3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum(300, [7, 14]))  # False