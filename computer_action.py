import constants
import data_cards
import data_pile_cards
import random
import rules
import value_cards


def computerPlayerCanPlayCard():
    # Get list of computer hand cards
    hand_computer = data_cards.cardList(constants.HAND_COMPUTER)
    hand_copy = []
    hand_copy.extend(hand_computer)
    print(hand_copy)    # debugging

    # Get top pile card and value
    card_pile_top = data_pile_cards.getPileTopCard()
    card_pile_top_value = value_cards.getCardValue(card_pile_top)

    while len(hand_copy) != 0:
        num = random.randint(0, (len(hand_copy) - 1))
        print("num is", num)    # debugging
        card_to_play = hand_copy[num]
        hand_copy.pop(num)
        print("card is", card_to_play)    # debugging
        card_to_play_value = value_cards.getCardValue(card_to_play)

        if rules.checkCanPlayCard(card_to_play_value, card_pile_top_value) == True:
            print("Found card to play:", card_to_play)
            return card_to_play

    return print("ERROR no card to play found")    # debugging
