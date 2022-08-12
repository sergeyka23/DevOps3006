is_true = False
a = 2
b = 2.5
strOne = "one"
strThree = "Three"
names = ["chanan", "tom", "zach", "aharon"]
print(type(a == b))
if a < b != 1 or not strOne == "moshe" or strThree == "Three":
    print("a is smaller that b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("b bigger than 1")
else:
    print("Something")
# ###################################################33
name_to_find = "ariel"
if name_to_find in names:
    print(name_to_find + " is on the list")
elif name_to_find in names:
    print(name_to_find + " is not on the list")
name_to_find = "tom"
if name_to_find in names:
    print(name_to_find + " on the list")
# ###########3
other_list = [""]
if len(other_list) > 0:
    print("other list has values")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
if (type(k) is int):
    print("int")
elif (type(k) is str):
    print("str")
print(type(k) is int)
print(k == f)
print(k is f)
print(t == e)
print(t is e)
