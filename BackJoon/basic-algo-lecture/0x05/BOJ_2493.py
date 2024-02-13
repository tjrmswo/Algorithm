# 정리: N개의 높이가 다른 레이저 송수신기가 있고 이 것은 왼쪽으로 레이저를 발사한다.
# 발사한 레이저는 자신보다 높은 위치에 있는 수신기가 수신한다.
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능
# 각각의 탑들에서 발사한 레이저 신호를 수신한 탑들의 번호를 하나의 빈칸을 사이에 두고 출력한다.

N = int(input())
susin = list(map(int, input().split()))
stack = []
max_N = 0

for i in range(len(susin)):
    copy = susin.copy()
    while len(copy) > 0:
        max_N = copy.pop()
        if susin[i] < max_N and susin.index(susin[i]) > susin.index(max_N):
            stack.append(susin.index(max_N) + 1)
            break
        else:
            continue
    else:
        stack.append(0)
print(stack)

# 현재 값은 잘 나오는데 시간 초과가 발생한다..
# 애초에 기준에 부합하지 않은 값은 애초에 제외하면
# 해결된다는 것을 백준 질문 게시판을 통해 알게 됨

# 앞으로 탐색? 뒤로 탐색?
# 앞으로 탐색 - 스택을 이용하지 않음. 레이저의 방향이 왼쪽이기 떄문에 i가 증가하면서
# 자신보다 앞의 인덱스에 큰 값이 있는지 탐색. 그러면 인덱스 0은 어떡하냐 따로 조건을 걸어야 함
# 하지만 이렇게 따로 0 인덱스는 처리하지 않는 방향임
# 뒤로 탐색 - 인덱스 값과 배열에서 pop한 값을 비교해서 자기 자신보다 큰 값을 찾는 것
