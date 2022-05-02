# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

def add(a, b):
    return a+b

def min(a, b):
    return a-b

def div(a, b):
    return a//b # // 부호 사용시 정수 return

def mux(a, b):
    return a*b

def rem(a, b):
    return int(a%b)

def solution(a, b):
    print(add(a, b))
    print(min(a, b))
    print(mux(a, b))
    print(div(a, b))
    print(rem(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    solution(a, b)

    # 아래 처럼 한줄 출력 가능
    # a,b=map(int,input().split())
    # print(a+b,a-b,a*b,a//b,a%b,sep='\n')