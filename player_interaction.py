import data_read_write
import readchar

HAND_PLAYER = "data_mutable/player_hand.txt"
HAND_COMPUTER = "data_mutable/computer_hand.txt"


def displayHand(docHandToDisplay):
    cards_in_hand = data_read_write.readFromFile(docHandToDisplay)
    print("Here are your cards:\n" + cards_in_hand)


def displayPlayerHand():
    displayHand(HAND_PLAYER)
