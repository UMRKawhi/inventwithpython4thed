import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    === ''', '''
 +---+
 o   |
     |
     |
    ===''', '''
 +---+
 o   |
 |   |
     |
    ===''', '''
 +---+
 o   |
 /|  |
     |
    ===''', '''
 +---+
 o   |
/|\  |
     |
    ===''', '''
 +---+
 o   |
/|\  |
/    |
    ===''', '''
 +---+
 o   |
/|\  |
/ \  |
    ===''']

# test the format of hangman ASCII
# for i in range(len(HANGMAN_PICS)):
#     print(HANGMAN_PICS[i])

words = 'ant baboon badger bat ber beaver camel cat clam cobra cougar \
    coyote crow deer doog donkey duck eagle ferret fox frog goat goose hawk\
    lion lizard llama mole monkey moose mouse mule newt otter owl panda\
    parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
    skunk sloth snake spider stork swan tiger toad troout turkey turtle\
    weasel whale wolf wombat zebra'.split()
# print(words)

def getRandomWord(wordList):
    pass
