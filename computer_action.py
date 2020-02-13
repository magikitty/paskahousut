import constants
import data_cards
import data_pile_cards
import data_read_write
import random
import rules
import value_cards


def playCardComputer():
    if computerCardToPlay() != constants.ERROR_NO_CARD_TO_PLAY:
        card_play = computerCardToPlay()
        data_cards.removeCardFromHand(card_play, constants.HAND_COMPUTER)
        print(constants.MESSAGE_COMPUTER_PLAYED_CARD, card_play)
        if value_cards.cardValueToInt(card_play) == 10:
            rules.foldPile()
            # Write function to start computer's turn again
        else:
            data_read_write.addToFile("\n" + card_play, constants.PILE_CARDS)
            if rules.fourOfAKind() == True:
                rules.foldPile()
                # Write function to start computer's turn again


def computerCardToPlay():
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
    return constants.ERROR_NO_CARD_TO_PLAY
