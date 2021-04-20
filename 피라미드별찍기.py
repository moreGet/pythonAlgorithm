floor = 6

for i in range(0, floor):
    for j in range(0, (floor-1)-i):
        print(" ", end="")

    for j in range(0, int((floor/2))*i+1):
        print("*", end="")

    print()