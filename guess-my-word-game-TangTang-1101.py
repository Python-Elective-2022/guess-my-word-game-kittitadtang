
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
    for every letter in secret_word
      if letter in letters_guessed
        pass
      otherwise
        return False
      return True
    '''
    # FILL IN YOUR CODE HERE...
    for i in secret_word:
      if i in letters_guessed:
        pass
      else:
        return False
      return True


### Testcases
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    for every letter in secret word 
      if letter in letters_guessed
        word +1
        other wise
        word += "_"
        return word
    '''
    # FILL IN YOUR CODE HERE...
    Word = ""
    for i in secret_word:
      if i in letters_guessed:
        Word += i
        pass
      else:
        Word += "_"
    return Word
    
    
    
      
#Testcases
# print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(lettersGuessed):
    '''
    lettersNotGuessed = abcdefgh.....
    if a letter is guessed, remove that letter from letterNotGuessed
    '''
    # FILL IN YOUR CODE HERE...   
    lettersNotGuessed = "abcdefghijklmnopqrstuvwxyz"
    lettersGuessed = ''.join(map(str,lettersGuessed))
    for char in lettersGuessed:
      lettersNotGuessed = lettersNotGuessed.replace(char, "")
    return lettersNotGuessed

def convert(string):
  """
  list equals to []
  list [:0] equals to string
  return list
  """
  list1 = []
  list1[:0] = string
  return list1

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
    # FILL IN YOUR CODE HERE...
    print('Start Game!')
    Word = ""
    lettersGuessed = []
    numOfGuesses = 8
    gameOver = False
    print("Guess of a word that is", len(secret_word), "letters long.")
    while numOfGuesses != 0 and gameOver == False:
      print(' ', numOfGuesses, 'guesses left.')
      print('Letters left:', get_available_letters(lettersGuessed))
      guessing_letter = input("Guess a letter: ")
      if guessing_letter in lettersGuessed:
        lettersGuessed.append(guessing_letter)
        print('This letter has already been guessed: ', get_guessed_word(secret_word, lettersGuessed))
      elif guessing_letter in convert(secret_word):
        lettersGuessed.append(guessing_letter)
        print('Correct:', get_guessed_word(secret_word, lettersGuessed))
      else:
        lettersGuessed.append(guessing_letter)
        print('The secret word does not contain this letter: ', get_guessed_word(secret_word, lettersGuessed))
        numOfGuesses -= 1
      print('')
      Word = get_guessed_word(secret_word, lettersGuessed)
      gameOver = is_word_guessed(secret_word, lettersGuessed)
      
    if numOfGuesses == 0:
      print("You lost, game over :( ")
      print('The secret word was:', secret_word)
    else:
      print("You win!, well done")
        


def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()