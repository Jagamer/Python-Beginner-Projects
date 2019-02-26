import random
from time import sleep


score = 3
cheat = 0


while True:

    print("\n" * 30)
    print("Nehme Schere/Stein/Papier:", end=" ")
    humanPick = str(input())
    humanPick = humanPick.lower()
    if humanPick == "stein" or humanPick == "schere" or humanPick == "papier" \
            or humanPick == "cheat":
        sleep(0)
    else:
        exit()
    choises = ["stein", "schere", "papier"]
    computerPick = random.choice(choises)
    print("Computer: ", computerPick.upper())  # Achtung
    if humanPick == computerPick:
        print("Es ist ein unentschieden!")
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(10)
    elif (computerPick == "schere" and humanPick == "papier") or \
            (computerPick == "stein" and humanPick == "schere") or \
            (computerPick == "papier" and humanPick == "stein"):
        print("Du hast verloren")
        score -= 1
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(10)
    else:
        print("Du hast gewonnen")
        score += 1
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(0)

    if humanPick == "cheat":

        print("Wow")
        print("\n" * 100)
        cheat = input(
            "1: Always winning, \n2: Always tie, \n3: Always losing\n\n")
        cheat = int(cheat)
        break

while True:
    if cheat == 1:
        print("\n" * 100)
        humanPick = input("Nehme Stein/Schere/Papier:")
        humanPick = humanPick.lower()
        if humanPick == "stein" or humanPick == "schere" or \
                humanPick == "papier" or humanPick == "cheat":
            wow = 0
        else:
            exit()
        if humanPick == "papier":
            computerPick = "Stein"
        elif humanPick == "Stein":
            computerPick = "Schere"
        else:
            computerPick = "Papier"
        print("Computer: ", computerPick.upper())
        print("Du hast gewonnen")
        score += 1
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(0)
    else:
        break

while True:
    if cheat == 2:
        print("\n" * 100)
        humanPick = input("Nehme Stein/Schere/Papier:")
        humanPick = humanPick.lower()
        if humanPick == "stein" or humanPick == "schere" or \
                humanPick == "papier" or humanPick == "cheat":
            wow = 0
        else:
            exit()
        computerPick = humanPick
        print("Computer:", computerPick.upper())
        print("Es ist ein unentschieden")
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(0)
    else:
        break

while True:
    if cheat == 3:
        print("\n" * 100)
        humanPick = input("Nehme Stein/Schere/Papier:")
        humanPick = humanPick.lower()
        if humanPick == "stein" or humanPick == "schere" or \
                humanPick == "papier" or humanPick == "cheat":
            wow = 0
        else:
            exit()
        if humanPick == "papier":
            computerPick = "Schere"
        elif humanPick == "Stein":
            computerPick = "Papier"
        else:
            computerPick = "Stein"
        print("Computer: ", computerPick.upper())
        print("Du hast verloren")
        score -= 1
        print("Score: ", score)
        weiter = input("")
        if weiter == "":
            sleep(0)
        else:
            sleep(0)
    else:
        break
