

def problem3():
    # Problem Set 3: String Methods
    # Upper & Lower:
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

    text = "MAY THE FORCE BE WITH YOU."
    print(text.lower())

    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    # a. Convert the list into a single string.
    # b. Now, split the string at every occurrence of the letter 'a'.

    motto = ["Make", "haste", "slowly."] #a
    join_string = ' '.join(motto)
    print(join_string)

    #B
    split_motto = join_string.split('a')
    print(split_motto)

    # Replacing Words:
    # Modify the sentence: "Life is what happens when you are busy making other plans."
    # a. Replace "busy" with "distracted".
    # b. Replace "plans" with "mistakes".

    sentence = "Life is what happens when you are busy making other plans."
    word1 = sentence.replace('busy', 'distracted')
    sentence = word1
    word2 = sentence.replace('plans', 'mistakes')
    sentence = word2
    print(sentence)
