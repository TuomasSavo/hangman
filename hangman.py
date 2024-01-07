# Hirsipuu peli
import random

def hirsipuu():
    arvo    = random.randint(0,3)
    sanat   = ["misse", "peppi", "tuomas"]
    sana    = sanat[arvo]

    wrong   = 0
    stages = ["",
              "_____      ",
              "     |     ",
              "     0     ",
              "    /|\    ",
              "    / \    ",
              "           "]
    rletters = list(sana)
    board    = ["_"] * len(sana)
    win      = False
    print("Tervetuloa pelaamaan Hirsipuuta! Oletko valmis?")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Arvaa kirjain "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Voitit pelin!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Hävisit pelin! Parempi onni ensi kerralla. Sana oli {}.".format(sana))

hirsipuu()
