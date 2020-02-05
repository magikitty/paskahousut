import constants
import data_cards
import data_read_write
import rules
import value_cards


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ")", cards_to_number[i])


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
        card_number = int(input(constants.MESSAGE_CHOOSE_CARD_TO_PLAY))
        if 0 < card_number <= len(player_cards):
            card_played = player_cards[card_number - 1]
            return card_played


def playCard():
    ## DISPLAY
    displayPlayerHandNumbered()
    displayPileTopCard()

    ## PLAYER
    card_play = getInputCard()
    print("card", card_play)                                                # debugging
    card_play_value_string = value_cards.getCardValue(card_play)
    print("cardValueString", card_play_value_string)                        # debugging
    card_play_value_int = value_cards.convertValueToInt(card_play_value_string)
    print("cardValueInt", card_play_value_int)                              # debugging

    ## PILE
    card_pile = createPileTopCard()
    card_pile_value_string = value_cards.getCardValue(card_pile)
    card_pile_value_int = value_cards.convertValueToInt(card_pile_value_string)

    ## PLAYING
    # cardValueString = rules.convertValueToInt(card)
    player_can_play_card = rules.checkCanPlayCard(card_play_value_int, card_pile_value_int)
    print("rules.playerCanPlayCard", player_can_play_card)                     # debugging

    if player_can_play_card == True:
        data_cards.removeCardFromPlayerHand(card_play)
        data_read_write.addToFile("\n" + card_play, constants.PILE_CARDS)
        print(constants.MESSAGE_PLAYED_CARD, card_play)
    else:
        print(constants.MESSAGE_CANNOT_PLAY_CARD)
        processPlayerTurn()


def drawCardAndPlay():
    card = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card)
    print(constants.MESSAGE_DRAW_CARD + card)
    # Check from rules if can play card
    # If can, play card
    # Else call pickUpAllCardsInPile()
    data_read_write.addToFile("\n" + card, constants.PILE_CARDS)


def pickUpAllCardsInPile():
    cards_in_pile = data_read_write.readFromFile(constants.PILE_CARDS)
    data_read_write.addToFile("\n" + cards_in_pile, constants.HAND_PLAYER)
    data_read_write.clearFile(constants.PILE_CARDS)


def getInputAction():
    print(constants.MESSAGE_INSTRUCTIONS_INTERACTION)

    player_command_valid = False

    while player_command_valid == False: 
        player_command = input(constants.MESSAGE_CHOOSE_ACTION).lower()
        if player_command == "s" or player_command == "p" or player_command == "d" or player_command == "i" or player_command == "u":
            return player_command


def playerAction(player_command):
    if player_command == "s":
        displayPlayerHandNumbered()
    elif player_command == "p":
        print(constants.MESSAGE_PLAY_CARD)
        playCard()
    elif player_command == "d":
        print(constants.MESSAGE_DRAW_PLAY)
        drawCardAndPlay()
    elif player_command == "u":
        print(constants.MESSAGE_PICK_PILE)
        pickUpAllCardsInPile()
    elif player_command == "i":
        displayPileNumbered()


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
    if len(pile_list) > 0:
        return pile_list[-1]
    else:
        # Need a card with value 0 if the pile is empty, so player can play a card on the empty pile
        empty_pile_list = ["0"]
        print(constants.MESSAGE_PILE_EMPTY)
        return empty_pile_list[0]


def displayPileTopCard():
    print(constants.MESSAGE_TOP_CARD_IN_PILE)
    card_pile_top = createPileTopCard()
    if card_pile_top != "0":
        print(card_pile_top)


def processPlayerTurn():
    playerAction(getInputAction())


# Strip trailing whitespace from player hand
    # stripped_data = data_read_write.readFromFile(HAND_PLAYER).strip()
    # data_read_write.writeToFile(stripped_data, constants.HAND_PLAYER)
    # # print((data_read_write.readFromFile(HAND_PLAYER)).strip())
