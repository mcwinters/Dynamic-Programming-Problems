"""Write a function count_construct(target, word_bank) that accepts a target string and a list of strings. 
The function should return the number of ways that the target can be constructed by concatenating elements of the word_bank list. 
You may reuse elements of the word_bank as many times as needed."""

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
    
# Test Cases
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 4
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # 0