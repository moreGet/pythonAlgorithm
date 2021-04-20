floor = 6

for i in range(1, floor):
    for j in range(1, floor-i):
        print(" ", end="")

    for j in range(1, int(floor/2)*i-1):
        print("*", end="")

    print()
    