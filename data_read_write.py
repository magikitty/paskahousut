

def writeToFile(content, fileToWriteTo):
    doc = open(fileToWriteTo, "w")
    doc.write(content)


def readFromFile(fileToReadFrom):
    doc = open(fileToReadFrom, "r")
    return doc.read()


def countContent(contentToCount, fileToCountFrom):
    allContent = readFromFile(fileToCountFrom)
    return allContent.count(contentToCount)