def solution(record):
    answer = []
    idMap = {} # 딕셔너리( Python의 Map이랑 같음 )

    for reco in record:
        context = reco.split()
        opCode = context[0] # 명령어 가져옴
        
        if opCode == 'Enter' or opCode == 'Change':
            idValue = context[1] # 고유 값 가져옴
            nickName = context[2] # 해당 고객의 닉네임 가져옴
            idMap[idValue] = nickName # 딕셔너리에 idValue를 Key로 nickName 저장

    for reco in record:
        context = reco.split()
        opCode = context[0] # 명령어 가져옴
        idValue = context[1]
        actionMsg = ''

        if opCode == 'Enter':
            actionMsg = idMap[idValue] + '님이 들어왔습니다.'
        elif opCode == 'Leave':
            actionMsg = idMap[idValue] + '님이 나갔습니다.'

        if len(actionMsg) >= 1:
            answer.append(actionMsg)

    return answer
    
if __name__ == '__main__':
    name = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234','Enter uid1234 Prodo','Change uid4567 Ryan']
    print(solution(name))