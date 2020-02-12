# Import packages
import random
import data_cards
import data_player_name
import data_read_write
import player_interaction
import constants
import value_cards
import rules
import first_player


# Game() calls the functions that make the game run
def Game():
    ensureMutableDataExists()
    data_read_write.clearFile(constants.HAND_PLAYER)
    data_read_write.clearFile(constants.HAND_COMPUTER)
    data_read_write.clearFile(constants.PILE_CARDS)
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


def ensureMutableDataExists():
    data_read_write.ensureDirectoryExists("data_mutable")
    data_read_write.ensureFileExists("data_mutable/cards_in_deck.txt")
    data_read_write.ensureFileExists("data_mutable/cards_in_pile.txt")
    data_read_write.ensureFileExists("data_mutable/computer_hand.txt")
    data_read_write.ensureFileExists("data_mutable/player_hand.txt")
    data_read_write.ensureFileExists("data_mutable/player_name.txt")


def welcomePlayer():
    print(constants.MESSAGE_WELCOME)
    GetSaveName()
    print("Hello " + data_player_name.getPlayerName() + "!\n")


# Gets the player's name
def GetSaveName():
    player_name = input(constants.MESSAGE_ENTER_NAME)
    data_player_name.setPlayerName(player_name)


# GameLoop alternates between the player's and computer's turn
def GameLoop(player_first):
    print("The game loop has started.") # debugging
    game_over = False

    while game_over == False:
        # print("The game is not over!") # debugging
        if player_first == True:
            for _ in range(0, 6): # debugging: limited game to six turns
                player_interaction.displayPileTopCard()
                PlayerTurn()
                ComputerTurn()
        elif player_first == False:
            for _ in range(0, 6): # debugging: limited game to six turns
                # player_interaction.displayPileTopCard()
                ComputerTurn()
                PlayerTurn()
        break   # debugging
    
    game_over = True
    print("The game is over!") # debugging


# PlayerTurn starts player's turn
def PlayerTurn():
    print(constants.MESSAGE_PLAYER_TURN)
    data_cards.dealCardToPlayer()
    player_interaction.displayPlayerHandNumbered()
    player_interaction.displayPileTopCard()
    player_interaction.processPlayerTurn()


# ComputerTurn starts computer's turn
def ComputerTurn():
    print(constants.MESSAGE_COMPUTER_TURN)
    data_cards.dealCardToComputer()


# Entry point function
Game()
