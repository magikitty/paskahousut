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

    while rules.winCheck() == "":
        if player_first == True:
            # data_pile_cards.displayPileTopCard()
            turn.playerTurn()
            rules.winCheck()
            turn.computerTurn()
            rules.winCheck()
        elif player_first == False:
            # data_pile_cards.displayPileTopCard()
            turn.computerTurn()
            rules.winCheck()
            turn.playerTurn()
            rules.winCheck()

    print("The game is over!", rules.winCheck(), "has won the game!") # debugging


# Entry point function
# newGame()
continueGame()
