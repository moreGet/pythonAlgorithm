import collections

# 한명만 RETURN 조건
def solution(participant, completion):
    answer = []
    participant.sort() # 참여자
    completion.sort() # 완주자

    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

if __name__ == '__main__':
    p = ["leo", "kiki", "eden"]
    c = ["eden", "kiki"]
    print(solution(p, c))