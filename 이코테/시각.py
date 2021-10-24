n = (int(input('몇시? N : ')) + 1)
min = 60
sec = 60

count = 0

for i in range(n):
    for j in range(min):
        for k in range(sec):
            if '3' in str(i) + str(j) + str(k):
                count += 1
    
print(f'{count} 가지 입니다.')