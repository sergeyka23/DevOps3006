import ast
my_file = open("config.json")
a = "{'name': 'moshe'}"

c = dict(ast.literal_eval(my_file.read()))
if (c["name"]) == "sergey":
    print("current")

with open("name.txt") as my_file:
    for name in my_file.readlines():
        print(my_file.strip())
