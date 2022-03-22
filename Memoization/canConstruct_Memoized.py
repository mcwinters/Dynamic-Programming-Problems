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

# Test Cases
print(canConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # True
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
print(canConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # False