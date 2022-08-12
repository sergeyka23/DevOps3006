from arith import addition, sub
from get_data import get_numer
import datetime



def dec(function_to_run):
    def wrapper():
        print(datetime.datetime.now())
        print("moshe")
        function_to_run()
        print(datetime.datetime.now())

    return wrapper

@dec
def print_something():
    print("something")

@dec
def print_another():
    print("another")


print_something()