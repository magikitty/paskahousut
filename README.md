# Paskahousu: A CLI-based Game of Cards

A Finnish card game called Paskahousu.

## Overview

I developed this program as a hobby project to improve my programming skills. The project is written in Python. In this game the user can play a game of Paskahousu against the computer.

The game contains persistent data in the form of text files where data is saved during the game.
This allows the player to quit and then load their saved game. The game entry point is in paskahousu.py and the gameloop and other set up functions are stored in setup_game.py. The game uses a read-eval-print-loop (REPL) for the gameloop. The files are organized into an immutable data directory, mutable data directory, and the Python files.

There are many variations of Paskahousu and the rules below are the rules that I have always
played the game with. You can read more about Paskahousu [here](https://en.wikipedia.org/wiki/Paskahousu).

## Rules of Paskahousu

The main point of the game is to get rid of all the cards in your hand by playing them.
You start with 3 cards and each turn you can play 1 card.
Whenever you start a turn with less than 3 cards in your hand you will be dealt 1 card.
Generally you can play a card that has the same number or a higher number than the one on the pile.
If there are four cards with the same number on top of the pile then the pile folds.

However, there are several special cards with special abilities:

* 2: can be placed on any other card (even an A).
* 3: an invisible card that can be placed on anything, except an A. The other player has to beat the card under the 3.
* 7: can be placed on anything, except an A. Only cards less than or equal to 7 can be placed on a 7.
* 10: folds the pile and the player who folded gets another turn.
* A: beats all other cards in the game. Only an A or a 2 can be placed on top of an A.

## Get the Game

You can get the game and try it out by cloning the repository.

### To clone the repository:

`git clone https://github.com/magikitty/paskahousut.git`

### To run the game:

`python3 paskahousu.py`