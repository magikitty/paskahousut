import constants
import data_cards
import data_read_write
import value_cards

# Move
def displayPileTopCard():
    card_pile_top = createPileTopCard()
    if card_pile_top != "0":
        print(constants.MESSAGE_TOP_CARD_IN_PILE)
        print(card_pile_top)


# Move
def createPileList():
    pile_list = (data_read_write.readFromFile(constants.PILE_CARDS)).split("\n")
    return data_cards.tidyList(pile_list)

# Move
def displayPileNumbered():
    print(constants.MESSAGE_ALL_CARDS_IN_PILE)
    pile_list = createPileList()
    # reverse list order, so most recently played card is number 1
    pile_list.reverse()
    return data_cards.numberedCardList(pile_list)

# Move
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

# Move
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
