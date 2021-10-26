def solution(numbers, hand):
    answer = ''
    right = [3, 6, 9]

    lPos = 0
    rPos = 0

    # 처음 순서
    for num in numbers[0:2]:
        if num in right:
            answer += 'R'
            rPos = num
        else:
            answer += 'L'
            lPos = num

    numbers = numbers[2:]
    for num in numbers:
        mL = abs(num-lPos)
        mR = abs(num-rPos)
        dL = (mL // 3) + (mL % 3)
        dR = (mR // 3) + (mR % 3)

        if dL < dR:
            answer += 'L'
            lPos = num
        elif dL > dR:
            answer += 'R'
            rPos = num
        else:
            if hand == 'right':
                answer += 'R'
                rPos = num
            else:
                answer += 'L'
                lPos = num
    return answer

if __name__ == '__main__':
    number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand = 'right'
    print(solution(number, hand))


