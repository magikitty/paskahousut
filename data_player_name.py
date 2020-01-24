DATA_PLAYER_NAME = "data_mutable/player_name.txt"

# Create or overwrite DATA_PLAYER_NAME file with player's name
def setPlayerName(textPlayerName):
  f = open(DATA_PLAYER_NAME, "w")
  f.write(textPlayerName)

def getPlayerName():
  f = open(DATA_PLAYER_NAME, "r")
  return f.read()