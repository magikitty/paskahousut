def cardValueToInt(card):
    card_value_string = getCardValue(card)
    card_value_int = convertValueToInt(card_value_string)
    return card_value_int


def getCardValue(card):
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
    return card_value_int


def getCardSuite(card):
    card_suite = ""
    space_before_word = card.rfind(" ")
    starting_index = space_before_word + 1

    for i in range(starting_index, len(card)):
        char = card[i]
        card_suite += char
    return card_suite
