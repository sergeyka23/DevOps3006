import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    choice = input("Choose a number from 1 to chosen difficulty " + str(difficulty) + " : ")
    range_array = [x for x in range(1, difficulty + 1)]
    while choice not in str(range_array):
        print("Wrong input.")
        choice = input("Please choose a number from 1 to chosen difficulty " + str(difficulty) + " : ")
    return choice


def compare_results(choice1, secret_number):
    if int(choice1) == secret_number:
        return True
    else:
        return False


def play(in_difficulty=1):
    generated_secret = generate_number(in_difficulty)
    choice_from_user = int(get_guess_from_user(in_difficulty))
    if compare_results(choice_from_user, generated_secret):
        print("Your guess is correct")
        return True
    else:
        print("Your guess is NOT correct")
        return Flase

