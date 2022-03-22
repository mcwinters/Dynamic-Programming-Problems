# Each problem solved with Top Down Approach (Memoization). My tips for this strategy are as follows:

## Brute Force Recursion
1. Create sections with Base Case(s) based off inputs
2. Create recursive step

## Add Memoization
1. Add `cache = None` as argument to function
    - Then add following line to top of function to reset cache: `if cache == None: cache = {}`
2. Add `if x in cache: return cache[x]` to Base Case(s) section
3. Add cache as an argument to all recursive calls
4. Add `cache[x] = y` above wherever you return y
