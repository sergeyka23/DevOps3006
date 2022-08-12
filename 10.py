import ast
my_file = open("config.json")
configuration = dict(ast.literal_eval(my_file.read()))
