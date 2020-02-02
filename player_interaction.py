import data_read_write
import data_cards
import readchar
import getch
import constants


def displayPlayerHand():
    cards_in_hand = data_read_write.readFromFile(constants.HAND_PLAYER)
    print(constants.MESSAGE_SHOW_HAND + cards_in_hand)
    

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
    print(constants.MESSAGE_INSTRUCTIONS_INTERACTION)
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
        print(constants.MESSAGE_PLAY_CARD)
    elif char == "d":
        print(constants.MESSAGE_DRAW_PLAY)
    elif char == "i":
        print(constants.MESSAGE_PICK_PILE)


def processPlayerTurn():
    playerAction(getInput())


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ".", cards_to_number[i])


def playCard():
    card_list = (data_read_write.readFromFile(constants.HAND_PLAYER).split("\n"))
    print("The original list is:", card_list)              # debugging  
    print("The new tidy list is:", data_cards.tidyList(card_list))    # debugging
    numberedCardList(data_cards.tidyList(card_list))


def drawCardAndPlay():
    card = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card)
    print(constants.MESSAGE_DRAW_CARD + card)
    # Check from rules if can play card
    # If can, play card
    # Else call pickUpAllCardsInPile()
    data_read_write.addToFile(card + "\n", constants.PILE_CARDS)


def pickUpAllCardsInPile():
    cards_in_pile = data_read_write.readFromFile(constants.PILE_CARDS)
    data_read_write.addToFile("\n" + cards_in_pile, constants.HAND_PLAYER)
    data_read_write.clearFile(constants.PILE_CARDS)


# Strip trailing whitespace from player hand
    # stripped_data = data_read_write.readFromFile(HAND_PLAYER).strip()
    # data_read_write.writeToFile(stripped_data, constants.HAND_PLAYER)
    # # print((data_read_write.readFromFile(HAND_PLAYER)).strip())
