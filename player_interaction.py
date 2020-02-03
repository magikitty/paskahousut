import data_read_write
import data_cards
import readchar
import constants


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ".", cards_to_number[i])


def cardListPlayer():
    card_list = (data_read_write.readFromFile(constants.HAND_PLAYER).split("\n"))
    return data_cards.tidyList(card_list) 


def displayPlayerHandNumbered():
    print(constants.MESSAGE_SHOW_HAND)
    # card_list = (data_read_write.readFromFile(constants.HAND_PLAYER).split("\n"))
    numberedCardList(data_cards.tidyList(cardListPlayer()))


def getInputCard():
    player_cards = cardListPlayer()
    card_number_valid = False

    while card_number_valid == False: 
        card_number = int(input("\nEnter number of card you want to play: "))
        if 0 < card_number <= len(player_cards):
            card_played = player_cards[card_number - 1]
            print("You play the card:", card_played)
            return card_played
            # card_index = card_number - 1
            # print("card at index", card_index)
            # return card_index


def playCard():
    displayPlayerHandNumbered()
    card = getInputCard()
    data_cards.removeCardFromPlayerHand(card)
    print("Here is the new list of cards")   # debugging
    displayPlayerHandNumbered()              # debugging
    data_read_write.addToFile(card + "\n", constants.PILE_CARDS)


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


def getInputAction():
    print(constants.MESSAGE_INSTRUCTIONS_INTERACTION)

    player_command_valid = False

    while player_command_valid == False: 
        player_command = input("\nWhat do you want to do? ").lower()
        if player_command == "s" or player_command == "p" or player_command == "d" or player_command == "i":
            return player_command


def playerAction(player_command):
    if player_command == "s":
        displayPlayerHandNumbered()
    elif player_command == "p":
        print(constants.MESSAGE_PLAY_CARD)
    elif player_command == "d":
        print(constants.MESSAGE_DRAW_PLAY)
        drawCardAndPlay()
    elif player_command == "i":
        print(constants.MESSAGE_PICK_PILE)
        pickUpAllCardsInPile()


def createPileList():
    pile_list = (data_read_write.readFromFile(constants.PILE_CARDS)).split("\n")
    return data_cards.tidyList(pile_list)


def displayPileNumbered():
    print(constants.MESSAGE_ALL_CARDS_IN_PILE)
    pile_list = createPileList()
    # reverse list order, so most recently played card is number 1
    pile_list.reverse()
    return numberedCardList(pile_list)


def createPileTopCard():
    pile_list = createPileList()
    # return last card in the list, so it is the most recently played card
    return pile_list[-1]


def displayPileTopCard():
    print(constants.MESSAGE_TOP_CARD_IN_PILE)
    print(createPileTopCard())


def processPlayerTurn():
    playerAction(getInputAction())


# Strip trailing whitespace from player hand
    # stripped_data = data_read_write.readFromFile(HAND_PLAYER).strip()
    # data_read_write.writeToFile(stripped_data, constants.HAND_PLAYER)
    # # print((data_read_write.readFromFile(HAND_PLAYER)).strip())
