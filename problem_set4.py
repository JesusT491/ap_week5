

def problem4():
    # Problem Set 4: String Properties and Advanced Operations
    # Repetition:
    # Concatenate the word "Iteration" 7 times.

    word_iteration = 'Iteration '
    print(word_iteration * 7)

    # Word Search:
    # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

    wordcheck = 'moonlight'
    quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
    appears = wordcheck in quote
    print(appears) #there is no moonlight breh (returns -1)


    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
    # b. Count the number of times the letter 'i' appears in the same word/phrase.

    text2 = "Supercalifragilisticexpialidocious"
    print(len(text2)) #a

    #b
    print(text2.count('i'))


    #.find looks for a phrase without an error
    #.index looks for a phrase and expects it to be there (ALSO ONLY RETURNS A NUMBER)