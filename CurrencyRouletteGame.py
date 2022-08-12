import requests


def get_money_interval(difficulty=1):
    d = float(difficulty)
    response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/ils.json')
    t = float(response.json()['ils'])
    interval = [t - (5 - d), t + (5 - d)]
    return interval


def get_guess_from_user(interval=[1.0, 2.0]):
    guess = float(input("Please guess the currency value: "))
    if interval[0] <= guess <= interval[1]:
        return True
    else:
        return False


def play(difficulty2=1):
    interval1 = []
    interval1 = get_money_interval(difficulty2)
    if get_guess_from_user(difficulty2, interval1):
        print("Your guess is correct")
    else:
        print("Your guess is NOT correct")
