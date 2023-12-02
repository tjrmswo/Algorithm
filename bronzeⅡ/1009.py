# 컴퓨터 10대
# N번 데이터는 N번 컴퓨터, 1N번 데이터는 N번 컴퓨터
# 총 데이터의 개수는 a^b개의 형태로 주어짐. '마지막 처리될 컴퓨터의 번호를 출력'
# import sys
# input = sys.stdin.readline()
# N = int(input())
# for i in range(1,N+1):
#     A,B = map(int,input().split())
#     power = A**B
#     print(power % 10)

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)