"""Say that you are a traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
You only move down or right. In how many ways can you travel to the goal on a grid with dimensions m * n?"""

def gridTraveller(m, n, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if (m,n) in cache: return cache[(m,n)]  # if in cache, return
    if m == n == 1: return 1
    if m < 1 or n < 1: return 0
    
    # Recursive Step
    cache[(m,n)] = gridTraveller(m - 1, n) + gridTraveller(m, n - 1)  # enter both moves (down & right) into cache and return 
    return cache[(m,n)]

# Test Cases
print(gridTraveller(1,1))  # 1
print(gridTraveller(2,3))  # 3
print(gridTraveller(3,2))  # 3
print(gridTraveller(3,3))  # 6
print(gridTraveller(18,18))  # 2333606220