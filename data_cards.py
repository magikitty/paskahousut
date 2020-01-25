import data_read_write

DATA_ALL_CARDS = "data_immutable/all_cards.txt"
DATA_DECK = "data_mutable/cards_in_deck.txt"

# Copy cards from all_cards.txt to cards_in_deck.txt to populate the deck
def populateDeck():
    data_read_write.writeToFile(getAllCards(), DATA_DECK)


def getAllCards():
    doc = open(DATA_ALL_CARDS, "r")
    return doc.read()


# Returns card at given index number from DATA_ALL_CARDS
def getCardNumber(cardNumber):
    doc = open("data_immutable/all_cards.txt", "r")
    all_lines = doc.readlines()
    return all_lines[cardNumber]
