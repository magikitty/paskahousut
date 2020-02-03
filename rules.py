import player_interaction

test_card_to_play = "10 of Hearts" # debugging
test_pile_card_value = 5 # debugging


def getCardValue():
    card = test_card_to_play
    card_value = ""

    for char in card:
        if char != " ":
            card_value += char
        else:
            break

    print(card_value)   # debugging
    return card_value


def checkCanPlayCard():
    test_card_value = getCardValue()
    if test_card_value == "J" or test_card_value == "Q" or test_card_value == "K":
        print("letter cards")
    else:
        if int(test_card_value) >= int(test_card_top_pile_value):
            can_play_card = True
        else:
            can_play_card = False
        return can_play_card
