# ** 선택 정렬 **
# Desc - O(n^2)의 복잡도를 가지며, 비교할 데이터가 많아지면 비교 횟수도 많아진다.
# 데이터가 많을때 피해야 하는 정렬 알고리즘 이다.
# Flow - 비교할 데이터 중 가장 작은 값을 배열 가장 앞으로 보낸다.

# 구현 코드
temp = 0
cnt = 0
index = 0

intArray = [1, 9, 7, 8, 6, 5, 2, 4, 3, 0]

for i in range(0, len(intArray)):
    min = 9999

    for j in range(i, len(intArray)):
        if(min > intArray[j]):
            min = intArray[j]
            index = j
    # 2차 for문 내부에 들어가는것 보다는 연산이 좀 더 빠르다.
    temp = intArray[i]
    intArray[i] = intArray[index]
    intArray[index] = temp
        

print(intArray)