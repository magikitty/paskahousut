import data_read_write
import readchar

HAND_PLAYER = "data_mutable/player_hand.txt"
HAND_COMPUTER = "data_mutable/computer_hand.txt"
INSTRUCTIONS_INTERACTION = ("Press P to play a card from your hand.\n" +
    "Press D to draw a card and immediately play it.\n" +
    "Press I to pick up all cards in the pile.")


def displayHand(docHandToDisplay):
    cards_in_hand = data_read_write.readFromFile(docHandToDisplay)
    print("Here are your cards:\n" + cards_in_hand)


def displayPlayerHand():
    displayHand(HAND_PLAYER)


def getInput():
    while True:
        print(INSTRUCTIONS_INTERACTION)
        char = readchar.readchar().lower()
        if char == "p":
            print("You are playing a card from your hand")
        elif char == "d":
            print("You are drawing a card and playing it")
        elif char == "i":
            print("You are picking up all the cards in the pile")
        else:
            print("Please press one of the specified keys")   # why is this called??
        break
    print("Pressed key: " + char)
    return(char)
