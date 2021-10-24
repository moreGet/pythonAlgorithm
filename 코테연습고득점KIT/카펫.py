def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    temp = []
    for i in range(1, total):
        if total % i == 0:
            temp.append(i)

    for i in temp:
        for j in temp:
            if (i >= j) and (i * j == total) and ((i*2) + (j*2))-4 == brown:
                answer = [i, j]
                return answer

if __name__ == '__main__':
    b = 10
    y = 2
    print(solution(b, y))