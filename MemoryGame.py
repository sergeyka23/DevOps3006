import random
import time


def generate_sequence(difficulty=1):
    max_number = 101
    rand_arr = []

    for i in range(difficulty):
        rand_int = random.randint(1, max_number)
        rand_arr.append(rand_int)
    return rand_arr


def get_list_from_user(difficulty1=1):
    lst_choice = []
    print("Please enter " + str(difficulty1) + " numbers you remember:")
    for i in range(difficulty1):
        choice = int(input())
        lst_choice.append(choice)
    return lst_choice


def is_list_equal(lst_user, lst_rand):
    l1 = set(lst_user)
    l2 = set(lst_rand)
    if l1 == l2:
        return True
    else:
        return False


def play(difficulty2):
    print("Memory game starts remember the following numbers:")
    lst_from_rand = []
    lst_from_rand = generate_sequence(difficulty2)
    print(lst_from_rand)
    time.sleep(0.7)
    print("\n" * 100)
    list_from_user = get_list_from_user(difficulty2)
    if is_list_equal(list_from_user, lst_from_rand):
        print("Correct answer")
    else:
        print("Wrong answer")
