def solution(answers):
    result = []
    fs = [1, 2, 3, 4, 5]
    ss = [2, 1, 2, 3, 2, 4, 2, 5]
    ts = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answerCount = [0, 0, 0]
    
    for i in range(len(answers)):
        fsAnswer = i % 5
        ssAnswer = i % 8
        tsAnswer = i % 10

        if answers[i] == fs[fsAnswer]:
            answerCount[0] += 1
        if answers[i] == ss[ssAnswer]:
            answerCount[1] += 1
        if answers[i] == ts[tsAnswer]:
            answerCount[2] += 1

    topRank = max(answerCount)
    for idx in range(len(answerCount)):
        if answerCount[idx] == topRank:
            result.append(idx+1)
            
    return result

if __name__ == '__main__':
    p = [1,3,2,4,2]
    print(solution(p))