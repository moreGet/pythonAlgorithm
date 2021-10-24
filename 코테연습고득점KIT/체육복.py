def solution(n, lost, reserve):
    # 여벌 체육복을 가진 학생이 도난을 당한 경우는 차집합을 이용하여 미리 제거
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for i in new_lost: 
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
        else:
            n-=1
    return n

if __name__ == '__main__':
    n = 5
    lost = [3, 5]
    reserve = [2, 4]	
    # lost = [2, 4]
    # reserve = [1, 3, 5]
    print(solution(n, lost, reserve))