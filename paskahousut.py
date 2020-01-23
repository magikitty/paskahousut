welcome_message = "This is a simple game of Paskahousut. Get ready to play!"

print(welcome_message)


# Gets the player's name
def GetName():
    player_name = input("Enter your name: ")
    print("Hello " + player_name + "!")
    return player_name


GetName()
