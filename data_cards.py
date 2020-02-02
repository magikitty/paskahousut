import data_read_write
import data_mutable
import random
import constants

# Copy cards from all_cards.txt to cards_in_deck.txt to populate the deck
def populateDeck():
    data_read_write.writeToFile(getAllCards(), constants.DATA_DECK)


def getAllCards():
    doc = open(constants.DATA_ALL_CARDS, "r")
    return doc.read()


def getCardAtIndex(cardIndex):
    doc = open(constants.DATA_DECK, "r")
    all_lines = doc.readlines()
    return all_lines[cardIndex].strip("\n")


def getRandomCard():
    max_number = countCardsInDeck()
    random_number = random.randint(0, max_number - 1)
    random_card = getCardAtIndex(random_number)
    return random_card


def countCardsInDeck():
    amountCards = data_read_write.countContent(constants.COUNTER_CARDS, constants.DATA_DECK)
    return amountCards


def dealCardToPlayer():
    if testCanDeal(constants.HAND_PLAYER) == True:
        card = getRandomCard()
        print("*** Dealt card to player: " + card)
        data_read_write.addToFile(card + "\n", constants.HAND_PLAYER)
        removeCardFromDeck(card)


def dealCardToComputer():
    if testCanDeal(constants.HAND_COMPUTER) == True:
        card = getRandomCard()
        print("~~~ Dealt card to computer: " + card)
        data_read_write.addToFile(card + "\n", constants.HAND_COMPUTER)
        removeCardFromDeck(card)


def removeCardFromDeck(card):
    deck = open(constants.DATA_DECK, "r")
    cards_in_deck = deck.readlines()

    data_read_write.writeToFile("", constants.DATA_DECK)

    for line in cards_in_deck:
        if card not in line:
            new_deck = open(constants.DATA_DECK, "a")
            new_deck.write(line)


def removeCardFromPlayerHand(card):
    hand_player = open(constants.HAND_PLAYER, "r")
    cards_in_hand = hand_player.readlines()

    data_read_write.writeToFile("", constants.HAND_PLAYER)

    for line in cards_in_hand:
        if card not in line:
            new_hand_player = open(constants.HAND_PLAYER, "a")
            new_hand_player.write(line)


def testCanDeal(docHandToDealTo):
    amount_cards = data_read_write.countContent(constants.COUNTER_CARDS, docHandToDealTo)
    if amount_cards < 3:
        can_deal = True
        # print("This person can be dealt a card")  # debugging
    else:
        can_deal = False
    return can_deal


def tidyList(list_to_tidy):
    clean_list = []
    for i in range(0, len(list_to_tidy)):
        if len(list_to_tidy[i]) > 0:
            clean_list.append(list_to_tidy[i])
    return clean_list
