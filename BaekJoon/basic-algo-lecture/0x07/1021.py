# 큐 연산
# 1. 첫 원소를 뽑아냄. a1,...ak 였던 것이 a2,...,ak와 같이 됌
# 2. 왼쪽 으로 한 칸 이동 시킨다 a1,...ak가 a2,...,ak,a1이 된다.
# 3. 오른쪽 으로 한 칸 이동 시킨다 a1,...ak,가 ak,a1,...,ak-1가 된다.
# 큐에 처음 포함 되어 있던 수 N이 주어 지고, 지민이가 뽑아 내려고 하는
# 원소의 위치가 주어 지고, 그 원소를 주어진 순서 대로 뽑아 내는데 드는 2번,3번 연산의 최솟값
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
que = deque([i for i in range(1, N+1)])
count = 0

for i in arr:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) < len(que) / 2:
                while que[0] != i:
                    que.append(que.popleft())
                    count += 1
            else:
                while que[0] != i:
                    que.appendleft(que.pop())
                    count += 1
print(count)
