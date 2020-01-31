import data_read_write
# import readchar
import getch

HAND_PLAYER = "data_mutable/player_hand.txt"
HAND_COMPUTER = "data_mutable/computer_hand.txt"
PILE_CARDS = "data_mutable/cards_in_pile.txt"

INSTRUCTIONS_INTERACTION = (
    "Press S to show cards in your hand.\n"
    "Press P to play a card from your hand.\n" +
    "Press D to draw a card and immediately play it.\n" +
    "Press I to pick up all cards in the pile."
    )
MESSAGE_SHOW_HAND = "\nHere are your cards:\n"
MESSAGE_PLAY_CARD = "You are playing a card from your hand"
MESSAGE_DRAW_PLAY = "You are drawing a card and playing it"
MESSAGE_PICK_PILE = "You are picking up all the cards in the pile"


def displayHand(docHandToDisplay):
    cards_in_hand = data_read_write.readFromFile(docHandToDisplay)
    print(MESSAGE_SHOW_HAND + cards_in_hand)


def displayPlayerHand():
    displayHand(HAND_PLAYER)


# PROBLEM: pressing the wrong key skips the player's turn
def getInput():
    print(INSTRUCTIONS_INTERACTION)
    char = ""

    while char != "s" or "p" or "d" or "i":
        char = getch.getch()
        if char == "s" or "p" or "d" or "i":
            return char


# Using readchar
# def getInput():
#     print(INSTRUCTIONS_INTERACTION)
#     char = ""

#     while char != "s" or "p" or "d" or "i":
#         char = readchar.readchar().lower() 
#         if char == "s" or "p" or "d" or "i":
#             return char


def playerAction(char):
    if char == "s":
        displayPlayerHand()
    elif char == "p":
        print(MESSAGE_PLAY_CARD)
    elif char == "d":
        print(MESSAGE_DRAW_PLAY)
    elif char == "i":
        print(MESSAGE_PICK_PILE)


def processPlayerTurn():
    playerAction(getInput())


def pickUpAllCardsInPile():
    cards_in_pile = data_read_write.readFromFile(PILE_CARDS)
    data_read_write.addToFile("\n" + cards_in_pile, HAND_PLAYER)
