import data_read_write
import constants


def setPlayerName(textPlayerName):
    data_read_write.writeToFile(textPlayerName, constants.DATA_PLAYER_NAME)


def getPlayerName():
    return data_read_write.readFromFile(constants.DATA_PLAYER_NAME)
