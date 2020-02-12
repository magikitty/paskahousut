import constants
import data_cards
import data_read_write
import rules
import value_cards


def processPlayerTurn():
    playerAction(getInputAction())


def playerAction(player_command):
    # if player_command == "s":
    if player_command == constants.ACTION_SHOW_HAND:
        displayPlayerHandNumbered()
        processPlayerTurn()
    # elif player_command == "p":
    elif player_command == constants.ACTION_PLAY_CARD:
        if len(data_cards.cardList(constants.HAND_PLAYER)) > 0:
            print(constants.MESSAGE_PLAY_CARD)
            playCard()
        else:
            print("You don't have any cards left!") # debugging
    # elif player_command == "d":
    elif player_command == constants.ACTION_DRAW_PLAY:
        if len(data_cards.cardList(constants.DECK_CARDS)) > 0:
            print(constants.MESSAGE_DRAW_PLAY)
            drawCardAndPlay()
        else:
            print("There are no cards left in the deck. Do something else.") # debugging
            processPlayerTurn()
    # elif player_command == "u":
    elif player_command == constants.ACTION_PICK_PILE:
        if len(data_cards.cardList(constants.PILE_CARDS)) > 0:
            pickUpAllCardsInPile()
        else:
            print("There are no cards in the pile. Do something else.") # debugging
            processPlayerTurn()
    # elif player_command == "i":
    elif player_command == constants.ACTION_ALL_CARDS_IN_PILE:
        displayPileNumbered()


def getInputAction():
    print(constants.MESSAGE_INSTRUCTIONS_INTERACTION)

    player_command_valid = False

    while player_command_valid == False: 
        player_command = input(constants.MESSAGE_CHOOSE_ACTION).lower()
        if player_command == "s" or player_command == "p" or player_command == "d" or player_command == "i" or player_command == "u":
            return player_command


def playCard():
    ## DISPLAY
    displayPlayerHandNumbered()
    displayPileTopCard()

    ## PLAYER
    card_play = getInputCard()
    card_play_value_int = value_cards.cardValueToInt(card_play)

    ## PILE
    card_pile = createPileTopCard()
    card_pile_value_int = value_cards.cardValueToInt(card_pile)
    # If top card in pile is 3
    if card_pile_value_int == 3:
        card_pile_value_string = value_cards.getCardValue(cardUnderThree())
        card_pile_value_int = value_cards.convertValueToInt(card_pile_value_string)

    ## PLAYING
    player_can_play_card = rules.checkCanPlayCard(card_play_value_int, card_pile_value_int)

    if player_can_play_card == True:
        data_cards.removeCardFromPlayerHand(card_play)
        print(constants.MESSAGE_PLAYED_CARD, card_play)
        if card_play_value_int == 10:
            rules.foldPile()
            processPlayerTurn()
        else:
            data_read_write.addToFile("\n" + card_play, constants.PILE_CARDS)
            if rules.fourOfAKind() == True:
                rules.foldPile()
                processPlayerTurn()
    else:
        print(constants.MESSAGE_CANNOT_PLAY_CARD)
        processPlayerTurn()


def displayPlayerHandNumbered():
    print(constants.MESSAGE_SHOW_HAND)
    # card_list = (data_read_write.readFromFile(constants.HAND_PLAYER).split("\n"))
    numberedCardList(data_cards.tidyList(cardListPlayer()))


def displayPileTopCard():
    card_pile_top = createPileTopCard()
    if card_pile_top != "0":
        print(constants.MESSAGE_TOP_CARD_IN_PILE)
        print(card_pile_top)


def getInputCard():
    player_cards = cardListPlayer()
    card_number_valid = False

    while card_number_valid == False: 
        card_number = int(input(constants.MESSAGE_CHOOSE_CARD_TO_PLAY))
        if 0 < card_number <= len(player_cards):
            card_played = player_cards[card_number - 1]
            return card_played


def cardListPlayer():
    return data_cards.cardList(constants.HAND_PLAYER)


# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ")", cards_to_number[i])


def drawCardAndPlay():
    card_drawn = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card_drawn)
    print(constants.MESSAGE_DRAW_CARD + card_drawn)
    card_play_value_int = value_cards.cardValueToInt(card_drawn)
    card_pile_value_int = value_cards.cardValueToInt(createPileTopCard())

    player_can_play_card = rules.checkCanPlayCard(card_play_value_int, card_pile_value_int)

    if player_can_play_card == True:
        data_cards.removeCardFromPlayerHand(card_drawn)
        print(constants.MESSAGE_PLAYED_CARD, card_drawn)
        if card_play_value_int == 10:
            rules.foldPile()
            processPlayerTurn()
        else:
            data_read_write.addToFile("\n" + card_drawn, constants.PILE_CARDS)
    else:
        data_read_write.addToFile(card_drawn, constants.HAND_PLAYER)
        pickUpAllCardsInPile()


def pickUpAllCardsInPile():
    cards_in_pile = data_read_write.readFromFile(constants.PILE_CARDS)
    data_read_write.addToFile("\n" + cards_in_pile, constants.HAND_PLAYER)
    data_read_write.clearFile(constants.PILE_CARDS)
    print(constants.MESSAGE_PICK_PILE)


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


def cardUnderThree():
    pile_list = createPileList()
    pile_list.reverse()
    counter = 0

    while counter < len(pile_list):
        card_to_beat = pile_list[counter]
        counter += 1
        if value_cards.getCardValue(card_to_beat) != "3":
            return card_to_beat
    return "0"
