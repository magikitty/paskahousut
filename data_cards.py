import data_read_write
import data_mutable
import random

DATA_ALL_CARDS = "data_immutable/all_cards.txt"
DATA_DECK = "data_mutable/cards_in_deck.txt"
COUNTER_CARDS = "of"


# Copy cards from all_cards.txt to cards_in_deck.txt to populate the deck
def populateDeck():
    data_read_write.writeToFile(getAllCards(), DATA_DECK)


def getAllCards():
    doc = open(DATA_ALL_CARDS, "r")
    return doc.read()


def getCardNumber(cardNumber):
    doc = open(DATA_DECK, "r")
    all_lines = doc.readlines()
    return all_lines[cardNumber].strip("\n")


def getRandomCard():
    max_number = countCardsInDeck()
    random_number = random.randint(0, max_number)
    random_card = getCardNumber(random_number)
    return random_card


def countCardsInDeck():
    amountCards = data_read_write.countContent(COUNTER_CARDS, DATA_DECK)
    return amountCards
