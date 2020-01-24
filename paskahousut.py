welcome_message = "This is a simple game of Paskahousut. Get ready to play!"

print(welcome_message)


# Gets the player's name
def GetName():
    player_name = input("Enter your name: ")
    print("Hello " + player_name + "!")
    return player_name


#GameOver determines whether or not the game is over for testing purposes
# def GameOver():
#     counter = 0
#     for num in range(1-11):
#         if counter < 10:
#             GameOver = False
#             counter += 1
#             return GameOver
#         elif counter >= 10:
#             GameOver = True
#             return GameOver

# GameLoop alternates between the player's and computer's turn
def GameLoop():
    print("The game loop has started.")
    GameOver = False
    while GameOver == False:
        print("The game is not over!")
        PlayerTurn()
        ComputerTurn()
        break
    GameOver = True
    print("The game is over!")
    print("The game loop has ended.")


# PlayerTurn starts player's turn
def PlayerTurn():
    print("It's the player's turn!")


# ComputerTurn starts computer's turn
def ComputerTurn():
    print("It's the computer's turn!")


# Game() calls the functions that make the game run
def Game():
    GetName()
    GameLoop()


# Call Game() to start game
Game()
