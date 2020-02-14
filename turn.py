import computer_action
import constants
import data_cards
import data_pile_cards
import player_interaction


# PlayerTurn starts player's turn
def playerTurn():
    print(constants.MESSAGE_PLAYER_TURN)
    data_cards.dealCardToPlayer()
    player_interaction.displayPlayerHandNumbered()
    data_pile_cards.displayPileTopCard()
    player_interaction.processPlayerTurn()


# ComputerTurn starts computer's turn
def computerTurn():
    print(constants.MESSAGE_COMPUTER_TURN)
    data_cards.dealCardToComputer()
    computer_action.processComputerTurn()
