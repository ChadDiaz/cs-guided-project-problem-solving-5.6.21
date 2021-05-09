""" Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples:

csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
csWhereIsBob(["Bob", "Layla", "Kaitlin", "Patricia"]) ➞ 0
csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
Notes:

Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").
[execution time limit] 4 seconds (py3)

[input] array.string names

[output] integer """

def csWhereIsBob(names):
    """
    Understand:
    test case 1: 
    ["Sarah", "Chad", "Jimmy", "Orlando", "Bob", "Janna", "Nico", "Barry"]
    output = 4

    test case 2:
    ["Sarah", "Chad", "Jimmy", "Orlando", "Janna", "Nico"]
    output = -1

    Plan:
 need to iterate over the array, looking for any value == "Bob" and return that index if found. if not, return -1
    """
def csWhereIsBob(names):
    # look to see if "Bob is in the list"
    if "Bob" not in names:
        return -1
    else:
        index = names.index("Bob")
        return index



