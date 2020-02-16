# Fix circular dependency between modules by moving functionality out of paskahousut.py
# Paskahousut.py only calls menu() to start game

# Import package
import setup_game

# Entry point function
setup_game.menu()
