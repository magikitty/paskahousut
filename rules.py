import player_interaction

test_card_to_play = "Q of Hearts" # debugging
test_pile_card_value = 5 # debugging


def getCardValue():
    card = test_card_to_play
    card_value = ""

    for char in card:
        if char != " ":
            card_value += char
        else:
            break

    # print(card_value)   # debugging
    return card_value


def convertValueToInt():
    card_value = getCardValue()
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
