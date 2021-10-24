def solution(s):
    answer = len(s) # 어차피 답은 전체 문자열 보다 적음

    for i in range(1, int(len(s)/2)+1): # 전체 문자열 에 반 이상 되는 문자는 어차피 압축이 불가능.
        pos = 0 # 먼저 첫번째 문자열 부터 잘라야 하니...
        length = len(s) # answer와 최솟값 비교를 위해 필요

        while pos+i <= len(s): # 현재 비교대상 문자가 주어진 문자열 보다 클 수 가 없음 그리고 for문이 돌아가면서 압축을 위한 index가 늘어남
            unit = s[pos:pos+i] # 비교대상 문자 먼저 추출
            pos+=i # 다음 비교 피대상 문자 자리로 이동을 위해 unit 문자열 보다 앞으로 이동

            cnt = 0 # 압축 당한 문자열의 갯수를 누적
            while pos+i <= len(s): # 첫 짧은 문자를 주어진 문자열에 풀스캔 해야 하므로 비교대상 문자열 만큼 또 돌림
                if unit == s[pos:pos+i]: # 비교할 문자열 과 비교 당할 문자열을 비교해서 같으면 압축(cnt 1증가)
                    cnt+=1 # 압축 했다!
                    pos+=i # 다음 비교 문자(비교 할 문자 만큼 자리 이동 해야지..)
                else:
                    break # 압축 할 문자열이 없다면 이번 루프 종료

            if cnt > 0: # 뭔가 한번이라도 압축 했으면...
                length-= (i*cnt) # 해당 문자열 갯수 만큼 length 차감

                if cnt < 9: # 10번 미만으로 압축 했다면 정답에는 한자리 수로 압축 숫자가 쓰여짐
                    length+=1
                elif cnt < 99: # 10의 자리는 2자리니까..
                    length+=2
                elif cnt < 999: # 100의 자리는 3자리니까...
                    length+=3
                else: # 1000의 자리까지 가능하니까...
                    length+=4
        
        answer = min(answer, length) # 전부 탐색 하였을때 같은 패턴으로 가장 최소한의 압축을한 정답은..?

    return answer

if __name__ == '__main__':
    s='ababcdcdababcdcd'
    print(solution(s))