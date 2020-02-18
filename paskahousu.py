# Fix circular dependency between modules by moving functionality out of paskahousu.py
# Paskahousu.py only calls welcomeToGame() and menu() to start game

# Import package
import constants
import setup_game

def welcomeToGame():
    print(constants.MESSAGE_WELCOME)

# Game entry point
welcomeToGame()
setup_game.menu()
