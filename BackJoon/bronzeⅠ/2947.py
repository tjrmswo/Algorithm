# 나무조각 5개. 1~5 번호가 쓰여있음.
# 크기로 정렬하여서 1,2,3,4,5의 순서를 만들려고 한다.
# 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의
# 순서를 출력하는 프로그램 작성

N = list(map(int,input().split()))
while True:
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            tmp = N[i+1]
            N[i+1] = N[i]
            N[i] = tmp
            # N[i],N[i+1] = N[i+1], N[i]
            print(" ".join(map(str, N)))
    if N == [1,2,3,4,5]:
        break


