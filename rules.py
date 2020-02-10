import constants
import data_read_write
import player_interaction
import value_cards


def checkCanPlayCard(card_to_play, card_pile_top):
    if card_pile_top == 7:
        if card_to_play <= 7:
            can_play_card = True
        else:
            can_play_card = False
        return can_play_card

    else:
        if card_to_play == 2:
            can_play_card = True

        elif card_to_play == 3:
            if card_pile_top <= 13:
                can_play_card = True
            else:
                can_play_card = False

        elif card_to_play == 7 or card_to_play == 10:
            if card_pile_top <= 13:
                can_play_card = True
            else:
                can_play_card = False

        else:
            if card_to_play >= card_pile_top:
                can_play_card = True
            else:
                can_play_card = False
        
        return can_play_card


def foldDeckWithTen(card_10):
    data_read_write.clearFile(constants.PILE_CARDS)
    print(constants.MESSAGE_FOLD_PILE)


def fourOfAKind():
    pile_list = player_interaction.createPileList()
    pile_list.reverse()
    four_of_a_kind = False
    counter = 4
    print("pile_list[0] is", pile_list[0])      # debugging
    top_card_int = value_cards.cardValueToInt(pile_list[0])
    print("top_card_int is", top_card_int)      # debugging

    for i in range(1, counter):
        next_card_int = value_cards.cardValueToInt(pile_list[i])
        print("next_card_int is", next_card_int)      # debugging
        while top_card_int == next_card_int:
            counter -= 1
            print(counter)
            break
        if counter == 1:
            four_of_a_kind = True
    return four_of_a_kind
