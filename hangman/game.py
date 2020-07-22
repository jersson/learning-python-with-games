# Hangman game
#
import os

from word_generator import loadWords, chooseWord
from hangman import hangman, isWordGuessed, getGuessedWord, getAvailableLetters

FOLDER_PATH = os.path.dirname(os.path.realpath(__file__))
WORDLIST_FILENAME = "words.txt"


def main():
    file = '{}/{}'.format(FOLDER_PATH, WORDLIST_FILENAME)

    wordlist = loadWords(file)
    secretWord = chooseWord(wordlist)
    hangman(secretWord)


main()
