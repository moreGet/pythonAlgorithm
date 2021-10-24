import re

def solution(new_id):
    answer = ''

    # 1단계 소문자 변환
    new_id = new_id.lower()
    print('STEP-1 : ',new_id)

    # 2단계 조건 제거
    temp_id = ''
    for char in new_id:
        ordValue = ord(char)
        if (ordValue >= ord('a') and ordValue <= ord('z')) or (ordValue >= ord('0') and ordValue <= ord('9')) or char == '-' or char == '_' or char == '.':
            temp_id += char
    print('STEP-2 : ',temp_id)

    # 3단계 마침표 치환
    temp_id = re.sub('[.]{2,}', '.', temp_id)
    print('STEP-3 : ',temp_id)

    # 4단계 양끝 . 치환
    temp_id = temp_id.rstrip('.')
    temp_id = temp_id.lstrip('.')
    print('STEP-4 : ',temp_id)

    # 빈 문자열
    if len(temp_id) == 0:
        answer = 'aaa'
        print('STEP-5 : ',answer)
        return answer

    # 6단계 16자 이상 문자열 자르기
    if len(temp_id) >= 16:
        temp_id = temp_id[0:15].rstrip('.')
    print('STEP-6 : ',temp_id, ' size : ',len(temp_id))

    # 7단계 문자열 덫 붙히기
    while len(temp_id) <= 2:
        temp_id+=temp_id[len(temp_id)-1:len(temp_id)]
    print('STEP-7 : ',temp_id)
    answer = temp_id

    return answer

if __name__ == '__main__':
    s=[
        '...!@BaT#*..y.abcdefghijklm',
        'z-+.^.',
        '=.=',
        '123_.def',
        'abcdefghijklmn.p']
    
    for str in s:
        print(solution(str))
        pass

    # print(solution('z-+.^.'))