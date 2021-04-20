floor = 10

for i in range(1, floor+1): # 1 시작 이므로 +1을 해줘야함
    for j in range(floor-i):
        print(" ", end="")

    for j in range(i*2-1):
        print("*", end="")
    
    print()