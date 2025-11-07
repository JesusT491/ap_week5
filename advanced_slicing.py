

def Adv_Slicing():
    # Advanced Slicing:
    # Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
    # a. Extract the letters 'hij'.
    # b. Extract every second letter starting from 'a' to 'm'.
    # c. Reverse the entire string using slicing.

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(alphabet.find('hij')) #method 1
    hij_index = alphabet.index('hij') #directly looks for the index in a string
    print(hij_index)
    print(alphabet[0:13:2]) #every second letter
    print(alphabet[::-1]) #reverse


    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote.split()[-1])

    name = quote.find('John F. Kennedy')
    print(name)



