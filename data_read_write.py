

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
