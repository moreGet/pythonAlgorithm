def gcd(a, b):
    n = 1
    result = 0

    while n != 0:
        if a > b:
            n = a % b
        else :
            n = b % a

        result = b # n == 0 일 경우 최대 공약수
        a = b
        b = n

    return result

def lcm(a, b): # 최소 공배수
    return int(a * b / gcd(a, b))

a, b = map(int, input().split())
print(lcm(a, b))