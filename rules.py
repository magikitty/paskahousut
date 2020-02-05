import player_interaction
import data_cards


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
                can_play_card = False           # IMPLEMENT card_pile_top == 3

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
