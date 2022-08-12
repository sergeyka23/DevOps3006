import requests

print("moshe")
try:
    f = int(input("enter number: "))
    r = 5/0
except BaseException as e:
    print("somthing wrong, here more")
    print(e.args)
except ZeroDivisionError:
    print("cant divide zero")
except ValueError:
    print("enter a legal number")

print("haim")