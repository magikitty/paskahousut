import constants
import data_cards
import data_read_write
import value_cards


def displayPileTopCard():
    card_pile_top = getPileTopCard()
    if card_pile_top != "0":
        print(constants.MESSAGE_TOP_CARD_IN_PILE, "\n" + card_pile_top)
        if value_cards.cardValueToInt(card_pile_top) == 3:
            displayCardUnderThree()


def getPileList():
    pile_list = (data_read_write.readFromFile(constants.PILE_CARDS)).split("\n")
    return data_cards.tidyList(pile_list)


def displayPileNumbered():
    print(constants.MESSAGE_ALL_CARDS_IN_PILE)
    pile_list = getPileList()
    # reverse list order, so most recently played card is number 1
    pile_list.reverse()
    return data_cards.numberedCardList(pile_list)


def getPileTopCard():
    pile_list = getPileList()
    # return last card in the list, so it is the most recently played card
    if len(pile_list) > 0:
        return pile_list[-1]
    else:
        # Need a card with value 0 if the pile is empty, so player can play a card on the empty pile
        empty_pile_list = ["0"]
        print(constants.MESSAGE_PILE_EMPTY)
        return empty_pile_list[0]


def displayCardUnderThree():
    card_under_three = cardUnderThree()
    if card_under_three == "0":
        print(constants.MESSAGE_NO_CARDS_UNDER_3)
    else:
        print("(" + constants.MESSAGE_CARD_UNDER_3, card_under_three + ")")


def cardUnderThree():
    pile_list = getPileList()
    pile_list.reverse()
    counter = 0

    while counter < len(pile_list):
        card_to_beat = pile_list[counter]
        counter += 1
        if value_cards.getCardValue(card_to_beat) != "3":
            return card_to_beat
    return "0"
