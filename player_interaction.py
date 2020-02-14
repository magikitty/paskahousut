import constants
import data_cards
import data_pile_cards
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
            print(constants.MESSAGE_EMPTY_HAND)
    # elif player_command == "d":
    elif player_command == constants.ACTION_DRAW_PLAY:
        if len(data_cards.cardList(constants.DECK_CARDS)) > 0:
            print(constants.MESSAGE_DRAW_PLAY)
            drawCardAndPlay()
        else:
            print(constants.MESSAGE_EMPTY_DECK)
            processPlayerTurn()
    # elif player_command == "u":
    elif player_command == constants.ACTION_PICK_PILE:
        if len(data_cards.cardList(constants.PILE_CARDS)) > 0:
            pickUpAllCardsInPile()
        else:
            print(constants.MESSAGE_EMPY_PILE)
            processPlayerTurn()
    # elif player_command == "i":
    elif player_command == constants.ACTION_ALL_CARDS_IN_PILE:
        data_pile_cards.displayPileNumbered()


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
    data_pile_cards.displayPileTopCard()

    ## PLAYER
    card_play = getInputCard()
    card_play_value_int = value_cards.cardValueToInt(card_play)

    ## PILE
    card_pile = data_pile_cards.getPileTopCard()
    card_pile_value_int = value_cards.cardValueToInt(card_pile)
    # If top card in pile is 3
    if card_pile_value_int == 3:
        card_pile_value_string = value_cards.getCardValue(data_pile_cards.cardUnderThree())
        card_pile_value_int = value_cards.convertValueToInt(card_pile_value_string)

    ## PLAYING
    player_can_play_card = rules.checkCanPlayCard(card_play_value_int, card_pile_value_int)

    if player_can_play_card == True:
        data_cards.removeCardFromHand(card_play, constants.HAND_PLAYER)
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
    data_cards.numberedCardList(data_cards.tidyList(cardListPlayer()))


def getInputCard():
    player_cards = cardListPlayer()
    card_number_valid = False

    while card_number_valid == False:
        choose_card_num = input(constants.MESSAGE_CHOOSE_CARD_TO_PLAY)
        if choose_card_num.isdigit() == True:
            if 0 < int(choose_card_num) <= len(player_cards):
                card_played = player_cards[int(choose_card_num) - 1]
                return card_played


def cardListPlayer():
    return data_cards.cardList(constants.HAND_PLAYER)


def drawCardAndPlay():
    card_drawn = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card_drawn)
    print(constants.MESSAGE_DRAW_CARD + card_drawn)
    card_play_value_int = value_cards.cardValueToInt(card_drawn)
    card_pile_value_int = value_cards.cardValueToInt(data_pile_cards.getPileTopCard())

    player_can_play_card = rules.checkCanPlayCard(card_play_value_int, card_pile_value_int)

    if player_can_play_card == True:
        data_cards.removeCardFromHand(card_drawn, constants.HAND_PLAYER)
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
