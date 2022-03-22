# Each problem solved with Bottom Up Approach (Tabulation). My tips for this strategy are as follows:

## Create Table
1. Create table based on input either by `[None] * x` or list comprehension if needed
2. Enter seed value(s), usually in `table[0]`

## Fill Table
1. Iterate through table and use current table value to fill in future values
    - Make sure to avoid Index Errors!
