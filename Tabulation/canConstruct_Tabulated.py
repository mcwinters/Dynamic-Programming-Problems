"""Write a function can_construct(target, word_bank) that accepts a target string and a list of strings. 
The function should return a boolean indicating whether or not the target can be constructed by concatenating elements of the word_bank list. 
You may reuse elements of the word_bank as many times as needed."""

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
    
# Test Cases
print(canConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # True
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # True
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
print(canConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # False