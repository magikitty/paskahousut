import constants
import data_cards
import data_read_write
import value_cards


def playerGoesFirst():
    hand_player = data_cards.cardList(constants.HAND_PLAYER)
    hand_computer = data_cards.cardList(constants.HAND_COMPUTER)
    return playerWithLowestHand(lowestCardInHand(hand_player), lowestCardInHand(hand_computer))


def lowestCardInHand(hand_list):
    card_lowest = "15"

    for i in range(0, len(hand_list)):
        card_hand_value = value_cards.cardValueToInt(hand_list[i])
        card_lowest_value = value_cards.cardValueToInt(card_lowest)

        if card_hand_value < card_lowest_value:
            card_lowest = hand_list[i]

        elif card_hand_value == card_lowest_value:
            card_hand_suite = value_cards.getCardSuite(hand_list[i])
            card_lowest_suite = value_cards.getCardSuite(card_lowest)
            card_hand_suite_value = constants.card_suite_values[card_hand_suite]
            card_lowest_suite_value = constants.card_suite_values[card_lowest_suite]

            if card_hand_suite_value < card_lowest_suite_value:
                card_lowest = hand_list[i]

    return card_lowest


# compare player and computer lowest card
def playerWithLowestHand(card_lowest_player, card_lowest_computer):
    card_lowest_player_value = value_cards.cardValueToInt(card_lowest_player)
    card_lowest_computer_value = value_cards.cardValueToInt(card_lowest_computer)

    player_first = False

    if card_lowest_player_value < card_lowest_computer_value:
        player_first = True

    elif card_lowest_player_value == card_lowest_computer_value:
        card_lowest_player_suite = value_cards.getCardSuite(card_lowest_player)
        card_lowest_computer_suite = value_cards.getCardSuite(card_lowest_computer)

        if card_lowest_player_suite < card_lowest_computer_suite:
            player_first = True

    return player_first


    # hand_player_values = value_cards.listCardValues(hand_player)
    # hand_player_values.sort()
    # hand_computer_values = value_cards.listCardValues(hand_computer)
    # hand_computer_values.sort()
    # print("player hand values", hand_player_values)     # debugging
    # print("computer hand values", hand_computer_values)     # debugging
