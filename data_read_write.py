from pathlib import Path


def writeToFile(content, fileToWriteTo):
    doc = open(fileToWriteTo, "w")
    doc.write(content)


def readFromFile(fileToReadFrom):
    doc = open(fileToReadFrom, "r")
    return doc.read()


def addToFile(content, fileToAddTo):
    doc = open(fileToAddTo, "a")
    doc.write(content)


def countContent(contentToCount, fileToCountFrom):
    allContent = readFromFile(fileToCountFrom)
    return allContent.count(contentToCount)


def clearFile(docToClear):
    doc = open(docToClear, "w")
    doc.write("")


def ensureDirectoryExists(directoryPath):
    directory_exists = Path(directoryPath).exists()

    if directory_exists == False:
        Path(directoryPath).mkdir()


def ensureFileExists(filePath):
    file_exists = Path(filePath).exists()

    if file_exists == False:
        writeToFile("", filePath)
