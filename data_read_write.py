import constants
from pathlib import Path


def readFromFile(fileToReadFrom):
    doc = open(fileToReadFrom, "r")
    return doc.read()


def writeToFile(content, fileToWriteTo):
    doc = open(fileToWriteTo, "w")
    doc.write(content)
    doc.close()


def addToFile(content, fileToAddTo):
    doc = open(fileToAddTo, "a")
    doc.write(content)
    doc.close()


def clearFile(docToClear):
    doc = open(docToClear, "w")
    doc.write("")
    doc.close()


def countContent(contentToCount, fileToCountFrom):
    allContent = readFromFile(fileToCountFrom)
    return allContent.count(contentToCount)


def ensureDirectoryExists(directoryPath):
    directory_exists = Path(directoryPath).exists()

    if directory_exists == False:
        Path(directoryPath).mkdir()


def ensureFileExists(filePath):
    file_exists = Path(filePath).exists()

    if file_exists == False:
        writeToFile("", filePath)


def ensureMutableDataExists():
    ensureDirectoryExists("data_mutable")
    ensureFileExists("data_mutable/cards_in_deck.txt")
    ensureFileExists("data_mutable/cards_in_pile.txt")
    ensureFileExists("data_mutable/computer_hand.txt")
    ensureFileExists("data_mutable/player_hand.txt")
    ensureFileExists("data_mutable/player_name.txt")


# Clear text files for beginning of new game
def ensureFilesClear():
    clearFile(constants.HAND_PLAYER)
    clearFile(constants.HAND_COMPUTER)
    clearFile(constants.PILE_CARDS)
