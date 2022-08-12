def print_hello(name):
    greeting_wrd = "hello"
    print(f"{greeting_wrd} {name}")


print_hello("moses")
print_hello("davis")


def greet_name(name, excluded_name="mich", greeting_wrd="hello"):
    if name != excluded_name:
        return f"{greeting_wrd} {name}"


def multiply(x, y):
    result = x * y
    result2 = x + y
    return result, result2


#user_name = int(input("enteryour name: "))
# print(greet_name(user_name))
hop = multiply(10, 4)
print(f"{hop[0]}  {hop[1]}")
