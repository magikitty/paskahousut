import constants
import data_cards
import data_read_write
import value_cards


def pickFirstPlayer():
    hand_player = data_cards.cardList(constants.HAND_PLAYER)
    hand_computer = data_cards.cardList(constants.HAND_COMPUTER)

    card_lowest = "15"

    for i in range(0, len(hand_player)):
        card_hand_value = value_cards.cardValueToInt(hand_player[i])
        card_lowest_value = value_cards.cardValueToInt(card_lowest)
        print("1 the card value is", card_hand_value)     # debugging

        if card_hand_value < card_lowest_value:
            card_lowest = hand_player[i]
            print("2 the lowest card is", card_lowest)     # debugging

        elif card_hand_value == card_lowest_value:
            card_hand_suite = value_cards.getCardSuite(hand_player[i])
            print("3 card_hand_suite is", card_hand_suite)     # debugging
            card_lowest_suite = value_cards.getCardSuite(card_lowest)
            print("3 card_lowest_suite is", card_lowest_suite)     # debugging
            card_hand_suite_value = constants.card_suite_values[card_hand_suite]
            print("!!!! 3 value of suite is ", constants.card_suite_values[card_hand_suite])     # debugging
            card_lowest_suite_value = constants.card_suite_values[card_lowest_suite]

            if card_hand_suite_value < card_lowest_suite_value:
                card_lowest = hand_player[i]
            print("3 the lowest card is", card_lowest)     # debugging



    # hand_player_values = value_cards.listCardValues(hand_player)
    # hand_player_values.sort()
    # hand_computer_values = value_cards.listCardValues(hand_computer)
    # hand_computer_values.sort()
    # print("player hand values", hand_player_values)     # debugging
    # print("computer hand values", hand_computer_values)     # debugging
