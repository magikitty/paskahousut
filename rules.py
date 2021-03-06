import constants
import data_cards
import data_pile_cards
import data_player_name
import data_read_write
import player_interaction
import value_cards


def checkCanPlayCard(card_to_play_int, card_pile_top_int):
    if card_pile_top_int == 7:
        if card_to_play_int <= 7:
            can_play_card = True
        else:
            can_play_card = False
        return can_play_card

    else:
        if card_to_play_int == 2:
            can_play_card = True

        elif card_to_play_int == 3:
            if card_pile_top_int <= 13:
                can_play_card = True
            else:
                can_play_card = False

        elif card_to_play_int == 7 or card_to_play_int == 10:
            if card_pile_top_int <= 13:
                can_play_card = True
            else:
                can_play_card = False

        else:
            if card_to_play_int >= card_pile_top_int:
                can_play_card = True
            else:
                can_play_card = False
        
        return can_play_card


def foldPile():
    data_read_write.clearFile(constants.PILE_CARDS)
    print(constants.MESSAGE_FOLD_PILE)


def fourOfAKind():
    pile_list = data_pile_cards.getPileList()
    pile_list.reverse()
    four_of_a_kind = False
    counter = 4
    top_card_int = value_cards.cardValueToInt(pile_list[0])

    if len(pile_list) >= 4:
        for i in range(1, counter):
            next_card_int = value_cards.cardValueToInt(pile_list[i])
            while top_card_int == next_card_int:
                counter -= 1
                break
            if counter == 1:
                four_of_a_kind = True
        return four_of_a_kind


def winCheck():
    winner = ""
    deck_cards = data_cards.cardList(constants.DECK_CARDS)
    player_hand = data_cards.cardList(constants.HAND_PLAYER)
    computer_hand = data_cards.cardList(constants.HAND_COMPUTER)

    if len(deck_cards) == 0 and len(player_hand) == 0:
        winner = data_player_name.getPlayerName()
    elif len(deck_cards) == 0 and len(computer_hand) == 0:
        winner = "computer"

    return winner
