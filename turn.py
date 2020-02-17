import computer_action
import constants
import data_cards
import data_pile_cards
import player_interaction
import rules


# PlayerTurn starts player's turn
def playerTurn():
    print(constants.MESSAGE_PLAYER_TURN)
    data_cards.dealCardToPlayer()
    data_cards.displayAmountCardsInDeck()
    player_interaction.displayPlayerHandNumbered()
    data_pile_cards.displayPileTopCard()
    player_interaction.processPlayerTurn()


# ComputerTurn starts computer's turn
def computerTurn():
    if not constants.QUIT_GAME:
        print(constants.MESSAGE_COMPUTER_TURN)
        data_cards.dealCardToComputer()
        data_cards.displayAmountCardsInDeck()
        computer_action.processComputerTurn()


def playerHasTurn():
    if rules.winCheck() == "":
        player_has_turn = True
    else:
        player_has_turn = False
    return player_has_turn
