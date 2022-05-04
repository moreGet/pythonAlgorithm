def solution(id_list, report, k):

    id_dic = { id : [] for id in id_list } # 누굴 신고했는지
    repo_cnt = {  id : 0 for id in id_list  } # 신고를 얼마나 당했는지

    for r in report:
        temp = r.split(' ')
        source = temp[0] # 신고자
        target = temp[1] # 신고 당한 사람

        id_dic[source].append(target)
        repo_cnt[target] += 1

    # {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['frodo', 'muzi'], 'neo': []} # 이렇게 신고했다
    # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2} # 이렇게 신고를 당했다
    print(f"레포트 조건 {k}건 / 레포드 목록 : {repo_cnt}")
    print("레포터 :", id_dic)

    for key, value in repo_cnt.items(): # k 만큼 신고당한 횟수 조회
        if (value != k) and value != 0: # k만큼 신고 당하지 않았다면
            for id, value in id_dic.items():
                if key in value:
                    value.remove(key)

    answer = list(map(len, id_dic.values()))
    return answer

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 4

print(solution(id_list, report, k))