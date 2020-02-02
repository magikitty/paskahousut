import data_read_write
import data_cards
import readchar
import constants


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ".", cards_to_number[i])


def displayPlayerHandNumbered():
    print(constants.MESSAGE_SHOW_HAND)
    card_list = (data_read_write.readFromFile(constants.HAND_PLAYER).split("\n"))
    numberedCardList(data_cards.tidyList(card_list))


def playCard():
    displayPlayerHandNumbered()


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


def getInput():
    print(constants.MESSAGE_INSTRUCTIONS_INTERACTION)

    player_command_valid = False

    while player_command_valid == False: 
        player_command = input("What do you want to do? ").lower()
        if player_command == "s" or player_command == "p" or player_command == "d" or player_command == "i":
            return player_command


def playerAction(char):
    if char == "s":
        displayPlayerHandNumbered()
    elif char == "p":
        print(constants.MESSAGE_PLAY_CARD)
    elif char == "d":
        print(constants.MESSAGE_DRAW_PLAY)
        drawCardAndPlay()
    elif char == "i":
        print(constants.MESSAGE_PICK_PILE)
        pickUpAllCardsInPile()


def processPlayerTurn():
    playerAction(getInput())


# Strip trailing whitespace from player hand
    # stripped_data = data_read_write.readFromFile(HAND_PLAYER).strip()
    # data_read_write.writeToFile(stripped_data, constants.HAND_PLAYER)
    # # print((data_read_write.readFromFile(HAND_PLAYER)).strip())
