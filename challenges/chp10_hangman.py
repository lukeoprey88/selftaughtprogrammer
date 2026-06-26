def hangman(word):

    wrong = 0 # counter
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\\     ", "|     / \\     ", "|"]

  
    rletters = list(word) #rletters = remaining letters

    board = ["_"] * len(word)

    print(board)

    win = False

    print("Welcome to Hangman")

    while wrong < len(stages) - 1: # game is ongoing

        print("\n")
        msg = "Guess a letter: "
        char = input(msg)

        if char in rletters: # if a correct match
            cind = rletters.index(char)
            board[cind] = char # fill in letter to display
            rletters[cind] = '$' # cancel out letter
        else:
            wrong += 1

        print((" ".join(board))) # output board with spaces
        e = wrong + 1 # stage to print (will start on 1)
        print("\n".join(stages[0: e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board)) # print out final word
            win = True
            break

    if not win:
        print("\n". join(stages[0: wrong]))
        print("You lose! It was {}".format(word))

import random

words = ['one', 'eats', 'wasps']
randomWord = random.choice(words)

hangman(randomWord)