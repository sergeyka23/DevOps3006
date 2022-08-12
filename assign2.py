# A:
x = 1
y = 2
if x > y:
    print("BIG")
elif x == y:
    print("nothing")
else:
    print("small")

# B:
length = 5
for i in range(length):
    print(i)

# C:
season = 2
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("chosen number is out of range")

# D:
# the print will be 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# E:
age = 34
str_fn = "k"
curr = 3.46
didFlewAboard = True
apartNum = 6
wanted_result = 37.46
my_profile = [age, str_fn, curr, didFlewAboard, apartNum]
for val in my_profile:
    print(val)

if (my_profile[0] + my_profile[2]) != wanted_result:
    print("age currency addition is incorrect")
else:
    print("age currency addition is correct")


# F:
phone_num = int(input("please insert your Phone number: "))
print("phone number " + str(phone_num))


# G:
def hello():
    print("hello")


def calculate(a=5, b=3.2):
    print(a + b)


# H:
def printName(name="Sergey"):
    print(name)


def divNum(c=2):
    print(c / 2)


# I:
def sumNum(d=2, e=4):
    print(d + e)


def spaceString(str1="a", str2="b"):
    print(str1 + " " + str2)


# K:
height = 5
for i in range(height):
    str3 = "*"
    for j in range(i):
        str3 = str3 + "*"
    print(str3)

# L:
height_x = 7
for i in range(height_x):
    str4 = ""
    for j in range(height_x):
        if j == i or j == (height_x - i - 1):
            str4 = str4 + "*"
        else:
            str4 = str4 + " "
    print(str4)


# M:
def getNum():
    num = int(input("please insert number: "))
    return num


def sumDigs(d=13):
    str5 = str(d)
    sum1 = 0
    for digit in str5:
        sum1 = sum1 + int(digit)
    print(sum1)


sumDigs(getNum())
