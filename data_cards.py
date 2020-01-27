import data_read_write
import data_mutable
import random

DATA_ALL_CARDS = "data_immutable/all_cards.txt"
DATA_DECK = "data_mutable/cards_in_deck.txt"
COUNTER_CARDS = "of"
HAND_PLAYER = "data_mutable/player_hand.txt"
HAND_COMPUTER = "data_mutable/computer_hand.txt"


# Copy cards from all_cards.txt to cards_in_deck.txt to populate the deck
def populateDeck():
    data_read_write.writeToFile(getAllCards(), DATA_DECK)


def getAllCards():
    doc = open(DATA_ALL_CARDS, "r")
    return doc.read()


def getCardAtIndex(cardIndex):
    doc = open(DATA_DECK, "r")
    all_lines = doc.readlines()
    return all_lines[cardIndex].strip("\n")


def getRandomCard():
    max_number = countCardsInDeck()
    random_number = random.randint(0, max_number - 1)
    random_card = getCardAtIndex(random_number)
    return random_card


def countCardsInDeck():
    amountCards = data_read_write.countContent(COUNTER_CARDS, DATA_DECK)
    return amountCards


def dealCardToPlayer():
    card = getRandomCard()
    print("dealt card: " + card)
    data_read_write.writeToFile(card, HAND_PLAYER)
    removeCardFromDeck(card)


def removeCardFromDeck(card):
    deck = open(DATA_DECK, "r")
    cards_in_deck = deck.readlines()

    data_read_write.writeToFile("", DATA_DECK)

    for line in cards_in_deck:
        if card not in line:
            new_deck = open(DATA_DECK, "a")
            new_deck.write(line)


def dealCardToComputer():
    card = getRandomCard()
    data_read_write.writeToFile(card, HAND_COMPUTER)
    removeCardFromDeck(card)