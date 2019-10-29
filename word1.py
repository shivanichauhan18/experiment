def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    all_letters_left = string.ascii_lowercase
    letter_left=""
    for letter in all_letters_left:
        if letter not in letters_guessed:
            letter_left=letter_left+letter
    return letter_left
print get_available_letters(["s"])