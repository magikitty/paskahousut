import data_read_write
import data_cards
import readchar
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
MESSAGE_DRAW_CARD = "The card you have drawn is: "


def displayPlayerHand():
    cards_in_hand = data_read_write.readFromFile(HAND_PLAYER)
    print(MESSAGE_SHOW_HAND + cards_in_hand)
    

# PROBLEM: pressing the wrong key skips the player's turn
# def getInput():
#     print(INSTRUCTIONS_INTERACTION)
#     char = ""

#     while char != "s" or "p" or "d" or "i":
#         char = getch.getch()
#         if char == "s" or "p" or "d" or "i":
#             return char


# Using readchar
def getInput():
    print(INSTRUCTIONS_INTERACTION)
    char = ""
    charValid = False

    while charValid == False:
        char = readchar.readchar().lower()
        if char == "s" or char == "p" or char == "d" or char == "i":
            return char


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


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ".", cards_to_number[i])


def playCard():
    card_list = (data_read_write.readFromFile(HAND_PLAYER).split("\n"))
    print("The original list is:", card_list)              # debugging  
    print("The new tidy list is:", data_cards.tidyList(card_list))    # debugging
    numberedCardList(data_cards.tidyList(card_list))


def drawCardAndPlay():
    card = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card)
    print(MESSAGE_DRAW_CARD + card)
    # Check from rules if can play card
    # If can, play card
    # Else call pickUpAllCardsInPile()
    data_read_write.addToFile(card + "\n", PILE_CARDS)


def pickUpAllCardsInPile():
    cards_in_pile = data_read_write.readFromFile(PILE_CARDS)
    data_read_write.addToFile("\n" + cards_in_pile, HAND_PLAYER)
    data_read_write.clearFile(PILE_CARDS)


# Strip trailing whitespace from player hand
    # stripped_data = data_read_write.readFromFile(HAND_PLAYER).strip()
    # data_read_write.writeToFile(stripped_data, HAND_PLAYER)
    # # print((data_read_write.readFromFile(HAND_PLAYER)).strip())
