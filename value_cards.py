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
