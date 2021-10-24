def solution(numbers):
    nStr = list(map(str, numbers)) # 각 요소 String값으로 변환후 리스트에 넣기
    nStr.sort(key = lambda x:x*3, reverse=True) # 각 문자로 변환된 숫자를 3개씩 붙혀서 리스트에 넣고 정렬(아스키 값 비교를 위해)
    return str(int(''.join(nStr))) # 0000문자열 일때 0으로 만들어 주기 위해 int로 변환후 다시 String으로 변환

if __name__ == '__main__':
    n = [6, 10, 2]
    print(solution(n))