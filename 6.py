names = ["chanan", "tom", "zach", "aharon"]
#range(1, 4, 1) range(17,2, -2)
for i in range(len(names)):
    print(names[i])

for name in names:
    print(name)
    if name == "zach":
        break

for name in names:
    if name == "zach":
        continue
    else:
        pass
    print(name)
    9
a = 0
while a < 5:
    print(a)
    a = a + 1
