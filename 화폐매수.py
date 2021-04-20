count = 0
coin = [500, 100, 50, 10]

money = 15660

for arg in coin:
    temp = int(money/arg)
    money%=arg
    count+=temp
    
    print(arg, '원 짜리 화폐 ', temp, '개')
    
print('동전 갯수 : ', count)