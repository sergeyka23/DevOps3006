from Score import add_score as user_won_add_score

def welcome(name):
    str6 = "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
    return str6


def load_game(user_won,prev_difficulty):

    welcome_text = [" 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
                    " 2. Guess Game - guess a number and see if you chose like the computer",
                    " 3. Currency Roulette - try and guess the value of a random amount of USD in ILS"]
    for i in range(len(welcome_text)):
        print(welcome_text[i])

    game_choice = input("Please choose a game to play: ")
    choice_max = len(welcome_text)
    array1 = [x for x in range(1, choice_max+1)]
    while game_choice not in str(array1):
        print("Wrong input.")
        game_choice = input("Please choose a game to play from 1 to 3: ")

    options = ["1. Memory Game ", "2. Guess Game", "3. Currency Roulette"]
    print("Your choice is: " + options[int(game_choice) - 1])
    print("Good choice!")

    game_difficulty = input("Please choose game difficulty from 1 to 5: ")
    difficulty_max = 5
    array2 = [x for x in range(1, difficulty_max+1)]

    while game_difficulty not in str(array2):
        print("Wrong input.")
        game_difficulty = input("Please choose game difficulty from 1 to 5: ")

    if user_won: user_won_add_score(prev_difficulty)

    print("Your difficulty choice is : " + game_difficulty)
    return game_choice, game_difficulty
