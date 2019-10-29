
def invalid(letters):
    if len(letters) > 1: #and letters == type(int):
        return False
    if not letters.isalpha():
        return False
    else:
        return True
    return sum
print invalid("t")


def get_hint(secret_word,letters_guessed):
    impoer random

    letter_list=[]
    index=0
    while index<len(secret_word):
        if secret_word[index] not in letters_guessed:
            if secret_word[index] not in letter_list:
                letter_list.append(secret_word[index])
        index=index+1
    print letter_list
    letter=random.choice(letter_list)
    return letter
print get_hint("shivani",["i","y"])


word_list = ["navgurukul", "learning", "kindness"]
    return word_list