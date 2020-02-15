# Data files
DATA_ALL_CARDS = "data_immutable/all_cards.txt"
DECK_CARDS = "data_mutable/cards_in_deck.txt"
DATA_PLAYER_NAME = "data_mutable/player_name.txt"
COUNTER_CARDS = "of"
HAND_PLAYER = "data_mutable/player_hand.txt"
HAND_COMPUTER = "data_mutable/computer_hand.txt"
PILE_CARDS = "data_mutable/cards_in_pile.txt"

# New game messages
MESSAGE_ENTER_NAME = "Enter your name: "
MESSAGE_WELCOME = "This is a simple game of Paskahousut. Get ready to play!"

MESSAGE_INSTRUCTIONS_INTERACTION = (
    "\n"
    "Press S to show cards in your hand.\n"
    "Press P to play a card from your hand.\n" +
    "Press D to draw a card and immediately play it.\n" +
    "Press U to pick up all cards in the pile.\n" +
    "Press I to inspect the cards in the pile"
    
    )

# Action messages
ACTION_ALL_CARDS_IN_PILE = "i"
ACTION_DRAW_PLAY = "d"
ACTION_PICK_PILE= "u"
ACTION_PLAY_CARD = "p"
ACTION_SHOW_HAND = "s"

# Action selection messages
MESSAGE_DRAW_CARD = "\nThe card you have drawn is: "
MESSAGE_DRAW_PLAY = "\nYou are drawing a card and playing it"
MESSAGE_PICK_PILE = "\nYou are picking up all the cards in the pile"
MESSAGE_PLAY_CARD = "\nYou are playing a card from your hand"
MESSAGE_SHOW_HAND = "\nHere are your cards:\n"

# Status messages for human player action
MESSAGE_CANNOT_PLAY_CARD = "\nYou cannot play that card. Choose another card or do something else."
MESSAGE_CHOOSE_ACTION = "\nWhat do you want to do? "
MESSAGE_CHOOSE_CARD_TO_PLAY = "\nEnter the number of the card you want to play: "
MESSAGE_EMPTY_DECK = "\nThere are no cards left in the deck. Do something else."
MESSAGE_EMPY_PILE = "\nThere are no cards in the pile. Do something else."
MESSAGE_FOLD_PILE = "\nThe pile has been folded."
MESSAGE_PLAYED_CARD = "\nYou play the card:"

# Status messages for human player
MESSAGE_ALL_CARDS_IN_PILE = "\nHere are all the cards in the pile. Card number 1 (at the top of the pile) is the most recent card played."
MESSAGE_AMOUNT_CARDS_DECK = "\nThe number of cards in the deck is:"
MESSAGE_CARD_UNDER_3 = "card to beat is:"
MESSAGE_EMPTY_HAND = "\nYou don't have any cards left in your hand!"
MESSAGE_NO_CARDS_UNDER_3 = "(There are no cards under 3)"
MESSAGE_PILE_EMPTY = "\nThere are no cards in the pile"
MESSAGE_PLAYER_TURN = "\nIt's the player's turn!"
MESSAGE_TOP_CARD_IN_PILE = "\nHere is the card at the top of the pile:"

# Status messages for computer player
MESSAGE_COMPUTER_PLAYED_CARD = "\nThe computer has played the card:"
MESSAGE_COMPUTER_TURN = "\nIt's the computer's turn!"
MESSAGE_COMPUTER_PICK_PILE = "\nComputer has picked up all the cards in the pile."

# Internal Message
INTERNAL_NO_CARD_TO_PLAY = "\nERROR: No card to play found\n"

# Dictionary with card suite values
card_suite_values = {"Clubs": 1, "Diamonds": 2, "Spades": 3, "Hearts": 4}
