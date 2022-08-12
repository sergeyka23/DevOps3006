for i in range(1, 101):
    if i % 7 != 0 and "7" not in str(i):
        print(i)
else: #will happen only if there was no break in the for
    print("loop finished successfully")