# Dynamic-Programming-Problems
Walkthrough of Dynamic Programming Problems in Python with both Memoization and Tabulation.
Thank you to @freeCodeCamp.org for [the course](https://youtu.be/oBt53YbR9Kk)!

## Memoization Strategy
### Brute Force Recursion
1. Create sections with Base Case(s) based off inputs
2. Create recursive step

### Add Memoization
1. Add `cache = None` as argument to function
    - Then add following line to top of function to reset cache: `if cache == None: cache = {}`
2. Add `if x in cache: return cache[x]` to Base Case(s) section
3. Add cache as an argument to all recursive calls
4. Add `cache[x] = y` above wherever you return y

## Tabulation Strategy
### Create Table
1. Create table based on input either by `[None] * x` or list comprehension if needed
2. Enter seed value(s), usually in `table[0]`

### Fill Table
1. Iterate through table and use current table value to fill in future values
    - Make sure to avoid Index Errors!

## Fibonacci Problem
"Write a function fib(n) that takes in a number as an argument. The function should return the n-th number of the Fibonacci sequence. 
The 0th number of the sequence is 0. The 1st number of the sequence is 1. To generate the next number of the sequence, we sum the previous two."

### Top-Down Approach (Memoization)
```
def fib(n, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    print(cache)
    if n in cache: return cache[n]  
    if n <= 1: return n
    
    # Recursive Step
    cache[n] = fib(n-1) + fib(n-2)  # update cache and return
    return cache[n]
```

### Bottom-Up Approach (Tabulation)
```
def fib(n):
    # Create Table
    dp = [None] * (n+1)  # initialize table full of None's
    dp[0], dp[1] = 0, 1  # input seed values
    
    # Fill Table
    for i in range(2, n+1):  # iterate through table
        dp[i] = dp[i-1] + dp[i-2]  # update table
        
    return dp[-1]
```

### Test Cases
```
print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025
```

## Grid Traveller Problem
"Say that you are a traveller on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right corner. 
You only move down or right. In how many ways can you travel to the goal on a grid with dimensions m * n?"

### Top-Down Approach (Memoization)
```
def gridTraveller(m, n, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if (m,n) in cache: return cache[(m,n)]  # if in cache, return
    if m == n == 1: return 1
    if m < 1 or n < 1: return 0
    
    # Recursive Step
    cache[(m,n)] = gridTraveller(m - 1, n) + gridTraveller(m, n - 1)  # enter both moves (down & right) into cache and return 
    return cache[(m,n)]
```

### Bottom-Up Approach (Tabulation)
```
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
```

### Test Cases
```
print(gridTraveller(1,1))  # 1
print(gridTraveller(2,3))  # 3
print(gridTraveller(3,2))  # 3
print(gridTraveller(3,3))  # 6
print(gridTraveller(18,18))  # 2333606220
```

## canSum Problem
"Write a function can_sum(target, numbers) that takes in a target and a list of numbers as arguments. 
The function should return a boolean indicating whether or not it is possible to generate the target using numbers from the list. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."

### Top-Down Approach (Memoization)
```
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
```

### Bottom-Up Approach (Tabulation)
```
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
```

### Test Cases
```
print(canSum(7, [2,3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum(300, [7, 14]))  # False
```

## howSum Problem
"Write a function how_sum(target, numbers) that takes in a target and a list of numbers as arguments. 
The function should return a list containing any combination of elements that add up to exactly the target. 
If there is no combination that adds up to the target, then return None. If there are multiple combinations possible, you may return any single one. 
You may use an element of the list as many times as needed. You may assume that all input numbers are nonnegative."

### Top-Down Approach (Memoization)
```
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
```

### Bottom-Up Approach (Tabulation)
```
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
```

### Test Cases
```
print(howSum(7, [2,3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None
```

## bestSum Problem
"Write a function best_sum(target, numbers) that takes in a target and a list of numbers as arguments. 
The function should return a list containing the shortest combination of numbers that add up to exactly the target.
If there a tie for the shortest combination, you may return any one of the shortest."

### Top-Down Approach (Memoization)
```
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
```

### Bottom-Up Approach (Tabulation)
```
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
```

### Test Cases
```
print(bestSum(7, [2,3]))  # [3, 2, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))  # None
print(bestSum(8, [2, 3, 5]))  # [5, 3]
print(bestSum(300, [7, 14]))  # None
```

## canConstruct Problem
"Write a function can_construct(target, wordBank) that accepts a target string and a list of strings. 
The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank list. 
You may reuse elements of the wordBank as many times as needed."

### Top-Down Approach (Memoization)
```
def canConstruct(target, wordBank, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]
    if target == "": return True
    
    # Recursive Step
    for word in wordBank:  # iterate through words
        if target.startswith(word) == True:  # if valid
            if canConstruct(target[len(word):], wordBank, cache) == True:  # if true, update cache and return
                cache[target] = True
                return True
    
    cache[target] = False  # update cache and return
    return False
```

### Bottom-Up Approach (Tabulation)
```
def canConstruct(target, wordBank):
    # Create Table
    dp = [False] * (len(target) + 1)
    dp[0] = True
    
    # Fill Table
    for i in range(len(target) + 1):  # iterate through table
        if dp[i] == True:
            for word in wordBank:  # iterate through words
                if (i + len(word) <= len(target)) and (target[i:i+len(word)] == word):  # avoid index error and check if valid
                    dp[i+len(word)] = True  # update table
    
    return dp[-1]
```

### Test Cases
```
print(canConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # True
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
print(canConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # False
```

## countConstruct Problem
"Write a function count_construct(target, wordBank) that accepts a target string and a list of strings. 
The function should return the number of ways that the target can be constructed by concatenating elements of the wordBank list. 
You may reuse elements of the wordBank as many times as needed."

### Top-Down Approach (Memoization)
```
def countConstruct(target, wordBank, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]
    if target == "": return 1
    
    count = 0
    
    # Recursive Step
    for word in wordBank:  # iterate through words
        if target.startswith(word) == True:  # if valid
            count += countConstruct(target[len(word):], wordBank, cache)  # increment count
            
    cache[target] = count  # update cache and return
    return count
```

### Bottom-Up Approach (Tabulation)
```
def countConstruct(target, wordBank):
    # Create Table
    dp = [0] * (len(target) + 1)
    dp[0] = 1
    
    # Fill Table
    for i in range(len(target) + 1):  # iterate through table
        for word in wordBank:  # iterate through words
            if target[i:i+len(word)] == word:  # if valid, update table
                dp[i+len(word)] += dp[i]
                    
    return dp[-1]
```

### Test Cases
```
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # 0
```

## allConstruct Problem
"Write a function all_construct(target, wordBank) that accepts a target string and a list of strings. 
The function should return a 2D list containing all the ways that the target can be constructed by concatenating elements of the wordBank list. 
Each element of the 2D list should represent one combination that constructs the target. You may reuse elements of the wordBank as many times as needed."

### Top-Down Approach (Memoization)
```
def allConstruct(target, wordBank, cache = None):
    if cache == None: cache = {}  # Workaround to have new cache for each testcase
    
    # Base Case(s)
    if target in cache: return cache[target]  # if already in cache, return
    if target == "": return [[]]  # if we have found target, return empty 2D array

    result = []  # initialize return array

    # Recursive Step
    for word in wordBank:  # iterate through words
        if target.startswith(word):  # check if current word applies
            suffix = target[len(word):]  # calculate rest of word
            suffixWays = allConstruct(suffix, wordBank, cache)  # recursive call
            targetWays = list(map(lambda l: [word] + l, suffixWays))  # append word to beginning of array
            result += targetWays  # add new combination to result array

    cache[target] = result  # add result to cache
    return result
```

### Bottom-Up Approach (Tabulation)
```
def allConstruct(target, wordbank):
    # Create Table
    dp = [[] for _ in range(len(target) + 1)]  # initialize table values as empty arrays
    dp[0] = [[]]  # initialize 1st element to empty 2D array

    # Fill Table
    for i in range(len(dp)):  # iterate through table
        for word in wordbank:  # iterate through words
            if target[i:i+len(word)] == word:  # if word is is valid
                dp[i+len(word)] += list(map(lambda l: l + [word], dp[i]))  # update table
                
    return dp[-1]  # return final element of table
```

### Test Cases
```
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
print(allConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []
```
