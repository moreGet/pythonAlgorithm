# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.
a = 2
b = 1

numb = []
while True:
    a, b = map(int, input().split())

    if a + b == 0:
        break

    numb.append([a, b])

numb = map(sum, numb)

for n in numb:
    print(n)
