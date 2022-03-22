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
    
# Test Cases
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # 0