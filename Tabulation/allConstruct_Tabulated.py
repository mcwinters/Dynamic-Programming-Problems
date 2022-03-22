"""Write a function all_construct(target, word_bank) that accepts a target string and a list of strings. 
The function should return a 2D list containing all the ways that the target can be constructed by concatenating elements of the word_bank list. 
Each element of the 2D list should represent one combination that constructs the target. You may reuse elements of the word_bank as many times as needed."""

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

# Test Cases
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # [['purp', 'le'], ['p', 'ur', 'p', 'le']]]
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [['ab', 'cd', 'ef'], ['ab', 'c', 'def'], ['abc', 'def'], ['abcd', 'ef']]
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # []
print(allConstruct("aaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))  # []
