"""Say that you are a traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
You only move down or right. In how many ways can you travel to the goal on a grid with dimensions m * n?"""

def gridTraveller(m,n):
    # Create Table
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[1][1] = 1
    
    # Fill Table
    for i in range(m+1):  # iterate through rows
        for j in range(n+1):  # iterate through columns
            current = dp[i][j] 
            if i + 1 <= m: dp[i+1][j] += current  # if valid, update table
            if j + 1 <= n: dp[i][j+1] += current  # if valid, update table
            
    return dp[-1][-1]

# Test Cases
print(gridTraveller(1,1))  # 1
print(gridTraveller(2,3))  # 3
print(gridTraveller(3,2))  # 3
print(gridTraveller(3,3))  # 6
print(gridTraveller(18,18))  # 2333606220