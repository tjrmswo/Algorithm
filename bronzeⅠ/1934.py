# 두 수 A와 B의 최소 공배수를 구해라
#
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    AA,BB = A,B

    while BB != 0:
        AA = AA % BB
        AA,BB = BB,AA
    print(A*B//AA)