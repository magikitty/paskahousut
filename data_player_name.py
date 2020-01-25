import data_read_write

DATA_PLAYER_NAME = "data_mutable/player_name.txt"


def setPlayerName(textPlayerName):
    data_read_write.writeToFile(textPlayerName, DATA_PLAYER_NAME)


def getPlayerName():
    return data_read_write.readFromFile(DATA_PLAYER_NAME)
