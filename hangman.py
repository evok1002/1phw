import random
import string
import copy
WORDLIST_FILENAME = "words.txt"
def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()
secret_word = choose_word(wordlist)
def is_word_guessed(secret_word, letters_guessed):
    secret_word = set(secret_word)
    letters_guessed = set(letters_guessed)
    intersection = secret_word & letters_guessed
    if intersection == secret_word:
        return True
    elif intersection != secret_word:
        return False

def get_guessed_word(secret_word, letters_guessed):
    sc = copy.deepcopy(secret_word)
    for i in sc:
        sc = sc.replace(i, "_ ")
    sc = sc.replace(" ", "")
    s = list(sc)
    for i in range(len(letters_guessed)):
        for j in range(len(secret_word)):
            if letters_guessed[i] == secret_word[j]:
                s[j] = letters_guessed[i]
    s = "".join(s)
    s = str(s)
    s = s.replace("_", "_ ")
    return s

def get_available_letters(letters_guessed):
    st = string.ascii_lowercase
    for i in range(len(letters_guessed)):
        for j in range(len(st)):
            if letters_guessed[i] == st[j]:
                st = st.replace(st[j]," ")
    st =st.replace(" ","")
    return st

def hangman(secret_word):
    pr="b, c, d, f, h, h, j, k,l, m, n, p, q, r, s, t, v, w, x, z"
    gl="a, e, i, o, u, y."
    print("Welcome to the game Hangman!\nI am thinking of a word that is",len(secret_word),"letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    warning = 3
    quesses = 6
    print("You have",quesses,"guesses left.")
    print("Available letters:",get_available_letters(""))
    letters_guessed = ""
    while True:
        letters = input("Please guess a letter: ")
        letters = letters.lower()
        while True:
            if letters.isalpha() != True or len(letters) > 1 or letters not in string.ascii_lowercase:
                warning -= 1
                if warning>0:
                    print("Oops! That is not a valid letter.You have", warning, "warnings left")
                    letters = input("Please guess a letter: ")
                elif warning <= 0:
                    quesses -= 1
                    if quesses <= 0:
                        break
                    else:
                        print("Oops! That is not a valid letter.You have", quesses, "guesses left.")
                        letters = input("Please guess a letter: ")
            else:
                break
        if letters in letters_guessed:
            warning -= 1
            if warning <=0:
                quesses -= 1
                print("Oops! You've already guessed that letter.You have", quesses, "guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break
            elif warning >0:
                print("Oops! You've already guessed that letter. You now have",warning,"warnings:")
                print(get_guessed_word(secret_word, letters_guessed))
        elif letters not in letters_guessed:
            letters_guessed += letters
            if letters in secret_word:
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Good guess:",get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word,letters_guessed):
                    print("Congratulations, you win!Your total score for this game is:",
                          quesses * len(set(secret_word)))
                    break
            elif letters not in secret_word and letters in pr:
                quesses-=1
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break
            elif letters not in secret_word and letters in gl:
                quesses-=2
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Oops! That letter is not in my word:",get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break


def match_with_gaps(my_word, other_word):
    mw = my_word.replace(" ", "")
    list1 = list(mw)
    if len(other_word) == len(mw):
        for i in range(len(mw)):
            if mw[i] == other_word[i]:
                continue
            elif mw[i] == "_" and other_word[i] not in list1:
                continue
            else:
                return False
        return True
    else:
        return False


def show_possible_matches(my_word):
    possible_matches = ""
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_matches += (other_word + " ")
        else:
            continue
    if possible_matches == "":
        print("No matches found")
    else:
        print(possible_matches)




def hangman_with_hints(secret_word):
    pr = "b, c, d, f, h, h, j, k,l, m, n, p, q, r, s, t, v, w, x, z"
    gl = "a, e, i, o, u, y."
    print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    warning = 3
    quesses = 6
    print("You have", quesses, "guesses left.")
    print("Available letters:", get_available_letters(""))
    letters_guessed = ""
    while True:
        letters = input("Please guess a letter: ")
        letters = letters.lower()
        while True:
            if letters != "*":
                if letters.isalpha() != True or len(letters) > 1 or letters not in string.ascii_lowercase:
                    warning -= 1
                    if warning > 0:
                        print("Oops! That is not a valid letter.You have", warning, "warnings left")
                        letters = input("Please guess a letter: ")
                    elif warning <= 0:
                        quesses -= 1
                        if quesses <= 0:
                            break
                        else:
                            print("Oops! That is not a valid letter.You have", quesses, "guesses left.")
                            letters = input("Please guess a letter: ")
                else:
                    break
            elif letters == "*" and "*" not in letters_guessed:
                print("Posible mathes:")
                show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                break
            else:
                print("You can't use help twice")
                letters = input("Please guess a letter: ")
        if letters in letters_guessed:
            warning -= 1
            if warning <= 0:
                quesses -= 1
                print("Oops! You've already guessed that letter.You have", quesses, "guesses left.")
                print(get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break
            elif warning > 0:
                print("Oops! You've already guessed that letter. You now have", warning, "warnings:")
                print(get_guessed_word(secret_word, letters_guessed))
        elif letters not in letters_guessed:
            letters_guessed += letters
            if letters in secret_word:
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed):
                    print("Congratulations, you win!Your total score for this game is:",
                          quesses * len(set(secret_word)))
                    break
            elif letters not in secret_word and letters in pr:
                quesses -= 1
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break
            elif letters not in secret_word and letters in gl:
                quesses -= 2
                print("You have", quesses, "guesses left.")
                print("Available letters:", get_available_letters(letters_guessed))
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                if quesses <= 0:
                    print("Sorry, you ran out of guesses. The word was else")
                    print(secret_word)
                    break
    pass



if __name__ == "__main__":

#   hangman(secret_word)
    hangman_with_hints(secret_word)

