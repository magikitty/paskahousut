# Import packages
import random
import data_cards
import data_player_name

# Welcome message for player
WELCOME_MESSAGE = "This is a simple game of Paskahousut. Get ready to play!"
print(WELCOME_MESSAGE)


# Gets the player's name
def GetSaveName():
    player_name = input("Enter your name: ")
    data_player_name.setPlayerName(player_name)


# Set first player (as Player or Computer) to start game
def SetFirstPlayer():
    start_num = random.randint(0, 1)
    player_first = False

    if start_num == 0:
        player_first = True

    return player_first


# GameLoop alternates between the player's and computer's turn
def GameLoop(player_first):
    print("The game loop has started.") # debugging
    game_over = False

    while game_over == False:
        print("The game is not over!") # debugging
        if player_first == True:
            PlayerTurn()
            ComputerTurn()
        elif player_first == False:
            ComputerTurn()
            PlayerTurn()
        break   # debugging
    
    game_over = True
    print("The game is over!") # debugging


# PlayerTurn starts player's turn
def PlayerTurn():
    print("It's the player's turn!")


# ComputerTurn starts computer's turn
def ComputerTurn():
    print("It's the computer's turn!")


# Game() calls the functions that make the game run
def Game():
    data_cards.populateDeck()
    GetSaveName()
    print("Hello " + data_player_name.getPlayerName() + "!")
    player_first = SetFirstPlayer()
    GameLoop(player_first)


# Entry point function
Game()
