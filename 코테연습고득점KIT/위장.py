def solution(clothes):
    answer = 1
    dicClothes = {}

    for clothe in clothes:
        if clothe[1] in dicClothes: # 현재 옷의 종류가 DIC에 있나?
            dicClothes[clothe[1]] += 1# 없으면 다른 종류니까 +1 연산하기
        else:
            dicClothes[clothe[1]] = 1 # 없는 종류면 세로운 KEY값으로 1넣어줌

    print(dicClothes)

    for i in dicClothes.values():
        answer *= (i+1)

    return answer - 1

if __name__ == '__main__':
    n = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(n))