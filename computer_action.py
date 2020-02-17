import constants
import data_cards
import data_pile_cards
import data_read_write
import random
import rules
import turn
import value_cards


def processComputerTurn():
    played_card = playCardComputer()
    if played_card == False:
        num = random.randint(0, 1)
        if num == 0 and len(data_cards.cardList(constants.DECK_CARDS)) > 0:
            drawPlayCardComputer()
        elif len(data_cards.cardList(constants.PILE_CARDS)) > 0:
            pickUpPileComputer()
        else:
            processComputerTurn()


def playCardComputer():
    card_play = cardToPlayComputer()
    if card_play != constants.INTERNAL_NO_CARD_TO_PLAY:
        data_cards.removeCardFromHand(card_play, constants.HAND_COMPUTER)
        print(constants.MESSAGE_COMPUTER_PLAYED_CARD, card_play)
        if value_cards.cardValueToInt(card_play) == 10:
            rules.foldPile()
            turn.computerTurn()
        else:
            data_read_write.addToFile("\n" + card_play, constants.PILE_CARDS)
            if rules.fourOfAKind() == True:
                rules.foldPile()
                turn.computerTurn()
        return True
    return False


def cardToPlayComputer():
    # Get list of computer hand cards
    hand_computer = data_cards.cardList(constants.HAND_COMPUTER)
    hand_copy = []
    hand_copy.extend(hand_computer)
    print(hand_copy)    # debugging

    # Get top pile card and value
    card_pile_top = data_pile_cards.getPileTopCard()
    card_pile_top_int = value_cards.cardValueToInt(card_pile_top)
    print("card to beat is:", card_pile_top_int)    # debugging
    # If top pile card = 3
    if card_pile_top_int == 3:
        card_pile_top_int = value_cards.cardValueToInt(data_pile_cards.cardUnderThree())
        print("card to beat is:", card_pile_top_int)    # debugging

    # Loop until card to play is found, else return error
    while len(hand_copy) != 0:
        num = random.randint(0, (len(hand_copy) - 1))
        print("num is", num)    # debugging
        card_to_play = hand_copy[num]
        hand_copy.pop(num)
        print("card is", card_to_play)    # debugging
        card_to_play_int = value_cards.cardValueToInt(card_to_play)

        if rules.checkCanPlayCard(card_to_play_int, card_pile_top_int) == True:
            print("Found card to play:", card_to_play)    # debugging
            return card_to_play

    print("ERROR no card to play found")    # debugging
    return constants.INTERNAL_NO_CARD_TO_PLAY


def drawPlayCardComputer():
    card_drawn = data_cards.getRandomCard()
    data_cards.removeCardFromDeck(card_drawn)
    print("Drew card:", card_drawn)     # debugging
    card_pile = data_pile_cards.getPileTopCard()

    card_drawn_int = value_cards.cardValueToInt(card_drawn)
    card_pile_int = value_cards.cardValueToInt(card_pile)

    if card_pile_int == 3:
        card_pile_value_string = value_cards.getCardValue(data_pile_cards.cardUnderThree())
        card_pile_int = value_cards.convertValueToInt(card_pile_value_string)

    computer_can_play_card = rules.checkCanPlayCard(card_drawn_int, card_pile_int)
    if computer_can_play_card == True:
        print(constants.MESSAGE_COMPUTER_PLAYED_CARD, card_drawn)
        if card_drawn_int == 10:
            rules.foldPile()
            turn.computerTurn()
        else:
            data_read_write.addToFile("\n" + card_drawn, constants.PILE_CARDS)
    else:
        data_read_write.addToFile("\n" + card_drawn, constants.HAND_COMPUTER)
        pickUpPileComputer()


def pickUpPileComputer():
    pile_cards = data_read_write.readFromFile(constants.PILE_CARDS)
    data_read_write.addToFile("\n" + pile_cards, constants.HAND_COMPUTER)
    data_read_write.clearFile(constants.PILE_CARDS)
    print(constants.MESSAGE_COMPUTER_PICK_PILE)
