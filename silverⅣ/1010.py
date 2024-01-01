# 사이트 = 강 주변 다리 짓기에 적합한 곳
# 서쪽엔 N개 동쪽엔 M개가 있는데, 사이트는 한 개의
# 다리만 연결될 수 있고, N개만큼 다리를 지으려고 할 때
# 다리는 서로 겹쳐질 수 없고 다리를 지을 수 있는
# 경우의 수를 구하는 프로그램을 작성

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    bridge = factorial(M) // (factorial(N)*factorial(M-N))
    print(bridge)
