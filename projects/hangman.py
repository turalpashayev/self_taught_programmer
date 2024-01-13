'''
It is text-based game called Hangman
Player 1 picks a secret word and draws line to represent each word
Player 2 tries to guess the word at a time.
If Player 2 guesses word correctly Player 1 replaces undescore with correct the letter
Otherwise Player 1 will draw a hang man.
If Player 2 guesses the word before hangman is complete then wins otherwise lose.
'''

def hangman(word):
    wrong = 0
    stages = ["",
              "_________       ",
              "|         ",
              "|    |    ",
              "|    O    ",
              "|   /|\\   ",
              "|   / \\   ",
              "|         ",
    ]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman game")

    while wrong < len(stages)-1:
        print("\n")
        message = "Guess a letter\n"
        char = input(message)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("\n You lose! Word was {} \n".format(word))

hangman('cat')