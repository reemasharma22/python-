inp = input ("Enter mark:")
mark = int(inp)
if mark>= 85:
    print("You have achieved a distinction!")
elif mark<= 65 and mark >85:
    print("You have passed")
else:
    print("You have failed")
