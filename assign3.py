from PIL import Image, ImageDraw

# 1: # 2:
try:
    a = 1 / 0
except ZeroDivisionError:
    print("cant divide zero")

# 3:
# Yes try can be handled with finally.

# 4:
# All types of exceptions

# 5:
# It will be hard to follow the exception in the code if no text involved
# No clear what was the cause for this exception

# 6: except IOError handles input/output operation fails, such as the print statement or the open() function when
# trying to open a file that does not exist. except ZeroDivisionError handles dvision by zero, an impossible
# mathematical operation.

# 7:
new_file = open("words.txt", "w")
new_file.close()

# 8:
new_file = open("words.txt", "a")
new_file.write("Sergey k." + "\n")
new_file.close()

# 9:
new_file = open("words.txt", "r")
for name in new_file.readlines():
    print(name, end='')
new_file.close()

# 10:
new_file = open("words.txt", "a", encoding="utf8")
new_file.write("בוקר טוב" + "\n")
new_file = open("words.txt", "r", encoding="utf8")
for name in new_file.readlines():
    print(name, end='')
new_file.close()

# 11:

width = 400
height = 300

img = Image.new('RGB', size=(width, height), color=(100, 10, 20))
d = ImageDraw.Draw(img)
d.text((165, 125), "Dev Expert", fill=(255, 255, 0))

img.save("image.png")
