# Paskahousu: A CLI-based game of cards

A Finnish card game called Paskahousu.

## Overview

TODO: Write overview.

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
