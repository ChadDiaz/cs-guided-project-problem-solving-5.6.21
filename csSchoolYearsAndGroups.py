"""
Imagine a school that children attend for years. In each year, there are a certain number of groups started, marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for the last year, the groups are 7a, 7b, 7c, 7d.

first year = 1a, 1b, 1c, 1d
second year = 2a, 2b, 2c, 2d,
ect....
7th year = 7a, 7b, 7c, 7d

Write a function that returns the groups in the school by year (as a string), separated with a comma and space in the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

Examples:

csSchoolYearsAndGroups(years = 7, groups = 4) ➞ "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"
Notes:

1 <= years <= 10
1 <= groups <=26
[execution time limit] 4 seconds (py3)

[input] integer years

[input] integer groups

[output] string
"""
def csSchoolYearsAndGroups(years, groups):
    """
    Understand:
    test case 1:
    6 years
    3 groups
    expected output =
    "1a, 1b, 1c, 2a, 2b, 2c, 3a, 3b, 3c, etc...6a, 6b, 6c"

    Plan:
    Given that the number of groups cannot be greater than the number of letters in the alphabet, each number should be assigned to the corresponding letter of the alphabet.

    assigned each letter of the alphabet to it's corresponding number to equal the groups input. 

    create an empty list
    loop through the years
    loop through the groups
    assign groups to a letter corresponding to the number
    concatenate and return ", " the results

    for (i = 1, i < whatever.length, i ++)
    """
    returnedList = []

    # this is going to loop through the years:
    for y in range(1, years + 1):

        # this will loop through the groups:
        for g in range(1, groups + 1):
            returnedList.append(str(y) + chr(g + 96))
    
    return ", ".join(returnedList)