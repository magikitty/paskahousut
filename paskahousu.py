# Import packages
import constants
import data_read_write
import setup_game

# Prints welcome message
def welcomeToGame():
    print(constants.MESSAGE_WELCOME)

# Game entry point
welcomeToGame()
setup_game.menu()
