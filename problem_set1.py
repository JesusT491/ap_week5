# Functions allow us to bundle code into a resuable blocks, making it easier to understand
# Prevents code duplciation as well

# Two steps to interact with a function
# Note: Use pass to avoid syntax error

# Define a function
def problem1():
    # Problem Set 1: Indexing and Slicing Strings
    # Basic Indexing:
    # Given the string magic = 'abracadabra',
    # a. Retrieve the 5th character.
    # b. Retrieve the second to last character.
    # c. Find the first occurrence of the letter 'c'.

    magic = 'abracadabra'
    print(magic[4]) #a also the first letter in the string is 0
    print(magic[9]) #b
    print(magic.find('c')) #c
 

# Calling a function