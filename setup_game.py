# Import packages
import constants
import computer_action
import data_cards
import data_pile_cards
import data_player_name
import data_read_write
import first_player
import player_interaction
import value_cards
import random
import rules
import turn


# Menu
def menu():
    print("It's a little menu!")    # debugging
    menuAction(menuInput())


def menuAction(menu_command):
    if menu_command == "n":
        print("You are starting a new game")    # debugging
        newGame()
    if menu_command == "l":
        print("You are loading your game")    # debugging
        loadGame()
    if menu_command == "r":
        print("You are looking at rules")    # debugging
        constants.RULES
    if menu_command == "q":
        print("You are quitting the game")    # debugging
        constants.QUIT_GAME = True


def menuInput():
    print(constants.MESSAGE_MENU_INSTRUCTIONS)
    menu_command_valid = False

    while menu_command_valid == False:
        menu_command = input("Press the key: ").lower()     # debugging
        if menu_command == "n" or menu_command == "l" or menu_command == "r" or menu_command == "q":
            return menu_command


# Game() calls the functions that make the game run
def newGame():
    data_read_write.ensureMutableDataExists()
    data_read_write.ensureFilesClear()
    data_cards.populateDeck()

    welcomePlayer()

    data_cards.dealCardToPlayer()
    data_cards.dealCardToPlayer()
    data_cards.dealCardToPlayer()
    data_cards.dealCardToComputer()
    data_cards.dealCardToComputer()
    data_cards.dealCardToComputer()
    data_cards.dealCardToComputer()

    print("player first is", first_player.playerGoesFirst())        # debugging
    GameLoop(first_player.playerGoesFirst())


def welcomePlayer():
    print(constants.MESSAGE_WELCOME)
    GetSaveName()
    print("Hello " + data_player_name.getPlayerName() + "!\n")


# Gets the player's name
def GetSaveName():
    player_name = input(constants.MESSAGE_ENTER_NAME)
    data_player_name.setPlayerName(player_name)


def loadGame():
    print(constants.MESSAGE_WELCOME_BACK, data_player_name.getPlayerName() + "!")
    GameLoop(first_player.playerGoesFirst())


# GameLoop alternates between the player's and computer's turn
def GameLoop(player_first):

    while rules.winCheck() == "" and constants.QUIT_GAME == False:
        if player_first == True:
            turn.playerTurn()
            rules.winCheck()
            turn.computerTurn()
            rules.winCheck()
        elif player_first == False:
            turn.computerTurn()
            rules.winCheck()
            turn.playerTurn()
            rules.winCheck()

    if rules.winCheck() != "":
        print("The game is over!", rules.winCheck(), "has won the game!") # debugging
