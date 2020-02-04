import player_interaction
import data_cards

# test_card_to_play = "10 of Hearts" # debugging
test_pile_card_value = 7 # debugging


def getCardValue(card):
    print("card is", card)
    card_value = ""

    for char in card:
        if char != " ":
            card_value += char
        else:
            break
    return card_value


def convertValueToInt(card_value):
    if card_value == "J":
        card_value_int = 11
    elif card_value == "Q":
        card_value_int = 12
    elif card_value == "K":
        card_value_int = 13
    elif card_value == "A":
        card_value_int = 14
    else:
        card_value_int = int(card_value)
    print("the int value of", card_value, "is", card_value_int)   # debugging
    return card_value_int


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
