

def problem2():
    # Problem Set 2: Extracting Information
    # From Descriptions:
    # Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

    quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
    print(quote.split()[-1])

    name = quote.find('John F. Kennedy')
    print(name)

    # Manipulating Words:
    # Given the string info = "Python is fun. Fun is good. Good is subjective.",
    # a. Extract the word 'subjective' without knowing its exact position.
    # b. Extract every third word.
    # c. Reverse the positions of the words, but keep the characters in each word in the same order.

    info = "Python is fun. Fun is good. Good is subjective."
    print(info.split()[-1]) #a
    print(info.split()[::3]) #b
    #c
    reverse_word_positions = info.split()[::-1]
    reverse_word_positions = ''.join(reverse_word_positions)
    print(reverse_word_positions)