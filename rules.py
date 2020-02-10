import constants
import data_read_write


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
