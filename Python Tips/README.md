# Here are some helpful methods + functions that I learned while solving these problems!

## String Slicing:
-	`String = “abcdef”`
-	`String[2:4] = “cd”`
    -	First index is inclusive, second is exclusive
-	Can leave either index blank to get all of the string until that point
    -	`String[:4] = “abcd”`

## Find a substring in a string
-	`find()` method
-	`string = “abcdef”`
-	`string.find(“def”)`
    -	Returns `4` (starting index of substring in string) or -1 if not found

## Check if string starts with substring
-	`startswith()` method
-	`String = “hello”`
-	`String.startswith(“hel”)`
    -	Returns `True`

## Create 2D array of 0’s
-	`zeros = [[0] * N for _ in range(M)]`

## Alter a list with a function
-	Use `list(map(lambda l: l + 1, [1,2,3]))`
    -	Returns `[2,3,4]`
-	Can use to add an element to 2d array
    -	`Arr = [[“ur”, “pl”, “e”]]`
    -	`newArr = list(map(lambda l: [“p”] + l, arr))`
        -	returns `[[“p”, “ur”, “pl”, “e”]]`
