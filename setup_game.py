# Import packages
import constants
import computer_action
import data_cards
import data_player_name
import data_read_write
import first_player
import rules
import turn


# Menu
def menu():
    menuAction(menuInput())


def menuAction(menu_command):
    if menu_command == constants.MENU_NEW_GAME:
        newGame()
    if menu_command == constants.MENU_LOAD_GAME:
        loadGame()
    if menu_command == constants.MENU_SEE_RULES:
        print(constants.RULES)
        menu()
    if menu_command == constants.MENU_QUIT:
        if quitInput() == constants.QUIT_YES:
            print(constants.MESSAGE_QUITTING)
            constants.QUIT_GAME = True
        else:
            menu()


def menuInput():
    print(constants.MESSAGE_MENU_INSTRUCTIONS)
    menu_command_valid = False

    while menu_command_valid == False:
        menu_command = input(constants.MESSAGE_CHOOSE_ACTION).lower()
        if menu_command == constants.MENU_NEW_GAME or menu_command == constants.MENU_LOAD_GAME or menu_command == constants.MENU_SEE_RULES or menu_command == constants.MENU_QUIT:
            return menu_command


def quitInput():
    quit_input_valid = False
    while quit_input_valid == False:
        quit_input = input(constants.MESSAGE_QUIT_INPUT).lower()
        if quit_input == constants.QUIT_YES or quit_input == constants.QUIT_NO:
            return quit_input


# newGame() calls the functions that make the game run
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

    gameLoop(first_player.playerGoesFirst())


def welcomePlayer():
    getSaveName()
    print("\nHello", data_player_name.getPlayerName() + "! Let's play!")


# Gets the player's name
def getSaveName():
    player_name = input(constants.MESSAGE_ENTER_NAME)
    data_player_name.setPlayerName(player_name)


# loadGame loads a previously started game
def loadGame():
    print(constants.MESSAGE_WELCOME_BACK, data_player_name.getPlayerName() + "!")
    gameLoop(first_player.playerGoesFirst())


# GameLoop alternates between the player's and computer's turn
def gameLoop(player_first):

    while rules.winCheck() == "" and constants.QUIT_GAME == False:
        if player_first == True:
            if turn.playerHasTurn() == True:
                turn.playerTurn()
            if turn.playerHasTurn() == True:
                turn.computerTurn()
        elif player_first == False:
            if turn.playerHasTurn() == True:
                turn.computerTurn()
            if turn.playerHasTurn() == True:
                turn.playerTurn()

    if rules.winCheck() != "":
        print(constants.MESSAGE_GAME_OVER, rules.winCheck() + "!")
