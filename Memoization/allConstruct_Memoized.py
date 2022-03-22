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

# Test Cases
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
print(allConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []