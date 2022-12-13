
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    """
    Pseudocode:

    for every letter in secret word
      if letter is not in letters_guessed
        return False
    otherwise return True
    """

    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True




### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''

    """
    Pseudocode:

    guessedWord = ""

    for each letter in secret_word
      if the letter is not in letters_guessed       
        print "_ " on guessedWord
      otherwise
        print letter on guessedWord
      return guessedWord
    """
    # FILL IN YOUR CODE HERE...
    
    guessedWord = ""
    for letter in secret_word:
      if letter not in letters_guessed:
        guessedWord += "_ "
      else:
        guessedWord += letter
    return guessedWord


#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    """
    Pseudocode:

    import string
    remainingLetters = string.ascii_lowercase (abcdefghi....)

    for any letter in letters_guessed
      remove from remainingLetters

    return remainingLetters
    """
    # FILL IN YOUR CODE HERE...   
    
    import string
    remainingLetters = string.ascii_lowercase

    for letter in letters_guessed:
        remainingLetters = remainingLetters.replace(letter, "")
    return remainingLetters
      


#Testcases 
# print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )

def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game.
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''

    """
    Pseudocode:

    numOfGuesses = 8
    letters_guessed = []
    end = False

    print ("Start Game!")
    print ("I am thinking of a word that is len(secret_word) letters long.")

    while numOfGuess is greater than 0 or game does not end yet:
      print('You Have', (numOfGuesses), 'guesses left')
      print('Letters available to you:', get_available_letters(letters_guessed))
      guess_a_letter = input("Guess a letter")

      if guess_a_letter is in letters_guessed
        print('You fool! You tried this letter already: ', get_guessed_word(secret_word, letters_guessed))
      otherwise
        add guess_a_letter to letters_guessed list
        if guess_a_letter is in the secret_word
          print('Correct: ', get_guessed_word(secret_word, letters_guessed))
        otherwise
          print('Incorrect, this letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
          decrese numOfGuesses by 1

      end = is_word_guessed(secret_word, letters_guessed)

    if is_word_guessed is the same as secret_word
      print("You Win! :) ")

    if numOfGuesses reaches 0
      print("Game Over!, You Lost :( ")
      print('The secret word was:', secret_word)


    """
    # FILL IN YOUR CODE HERE...
    print("Start Game!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    
    numOfGuesses = 8
    letters_guessed = []
    end = False

    while numOfGuesses > 0 and end == False:
      print('You have', numOfGuesses, 'guesses left')
      print('Letters available to you:', get_available_letters(letters_guessed))
      guess_a_letter = input("Guess a letter: ")

      if (guess_a_letter in letters_guessed) == True:
        print('You fool! You tried this letter already: ', get_guessed_word(secret_word, letters_guessed))
      else:
        letters_guessed.append(guess_a_letter)
        if (guess_a_letter in secret_word) == True:
          print('Correct:', get_guessed_word(secret_word, letters_guessed))
        else:
          print('Incorrect, this letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
          numOfGuesses -= 1

      end = is_word_guessed(secret_word, letters_guessed)

    if numOfGuesses == 0:
      print("Game Over!, You Lost :( ")
      print('The secret word was:', secret_word)

    if get_guessed_word(secret_word, letters_guessed) == secret_word:
      print("You Win! :)")
    


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()