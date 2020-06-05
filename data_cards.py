import data_read_write
import random
import constants

# Copy cards from all_cards.txt to cards_in_deck.txt to populate the deck
def populateDeck():
    data_read_write.writeToFile(getAllCards(), constants.DECK_CARDS)


def getAllCards():
    doc = open(constants.DATA_ALL_CARDS, "r")
    return doc.read()


def dealCardToPlayer():
    if len(cardList(constants.DECK_CARDS)) > 0 and testCanDeal(constants.HAND_PLAYER) == True:
        card = getRandomCard()
        print(constants.MESSAGE_DEALT_CARD, card)
        data_read_write.addToFile("\n" + card, constants.HAND_PLAYER)
        removeCardFromDeck(card)


def dealCardToComputer():
    if len(cardList(constants.DECK_CARDS)) > 0 and testCanDeal(constants.HAND_COMPUTER) == True:
        card = getRandomCard()
        data_read_write.addToFile("\n" + card, constants.HAND_COMPUTER)
        removeCardFromDeck(card)


def testCanDeal(docHandToDealTo):
    amount_cards = data_read_write.countContent(constants.COUNTER_CARDS, docHandToDealTo)
    if amount_cards < 3:
        can_deal = True
    else:
        can_deal = False
    return can_deal


def getRandomCard():
    max_number = countCardsInDeck()
    random_number = random.randint(0, max_number - 1)
    random_card = getCardAtIndex(random_number)
    return random_card


def countCardsInDeck():
    amountCards = data_read_write.countContent(constants.COUNTER_CARDS, constants.DECK_CARDS)
    return amountCards


def displayAmountCardsInDeck():
    print(constants.MESSAGE_AMOUNT_CARDS_DECK, countCardsInDeck())


def getCardAtIndex(cardIndex):
    doc = open(constants.DECK_CARDS, "r")
    all_lines = doc.readlines()
    return all_lines[cardIndex].strip("\n")


def removeCardFromDeck(card):
    deck = open(constants.DECK_CARDS, "r")
    cards_in_deck = deck.readlines()

    data_read_write.writeToFile("", constants.DECK_CARDS)

    for line in cards_in_deck:
        if card not in line:
            new_deck = open(constants.DECK_CARDS, "a")
            new_deck.write(line)


def removeCardFromHand(card, hand_file):
    hand_player = open(hand_file, "r")
    cards_in_hand = hand_player.readlines()

    data_read_write.writeToFile("", hand_file)

    for line in cards_in_hand:
        if card not in line:
            new_hand_player = open(hand_file, "a")
            new_hand_player.write(line)


def cardList(card_data_file):
    card_list = (data_read_write.readFromFile(card_data_file).split("\n"))
    return tidyList(card_list)


def tidyList(list_to_tidy):
    clean_list = []
    for i in range(0, len(list_to_tidy)):
        if len(list_to_tidy[i]) > 0:
            clean_list.append(list_to_tidy[i])
    return clean_list

# adding line numbers to cards
def numberedCardList(cards_to_number):
    for i in range(0, len(cards_to_number)):
        num = i + 1
        print(str(num) + ")", cards_to_number[i])
