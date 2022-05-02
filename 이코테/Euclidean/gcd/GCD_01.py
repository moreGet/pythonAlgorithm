# greatest_common_divisor (유클리드 호제법 gcd)
# 임의의 자연수 a, b가 주어졌을때 큰 값이 a라면 a%b = n 일떄 n이 0일때 b가 최대 공약수 이다
# 만약 n이 0이 아니라면 a에는 b값 b에는 n을 대입하고 반복한다.

def gcd(a, b):
    n = 1
    result = 0

    while n != 0:
        if a > b:
            n = a % b
        else:
            n = b % a

        # n != 0 이면
        result = b
        a = b # a = b
        b = n # b = n

    return result

a, b = map(int, input().split()) # a, b 입력

# 최대 공약수 알고리즘
print(gcd(a, b))