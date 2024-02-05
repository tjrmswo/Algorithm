# 피시방에는 1번부터 100번까지 컴퓨터가 있음
# 들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고 싶어함.
# 따라서 들어오면서 번호를 말하는데 자리에 사람이 없으면 앉아서 컴퓨터를 할 수 있고 있다면 거절당함.
# 거절 당하는 사람의 수를 출력하는 프로그램을 작성
# 자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없음.

# 1 2 3 2 3 2 5
N = int(input())
S = list(map(int,input().split()))
cnt = 0
seat = []
for i in range(N):
    if S[i] in seat:
        cnt += 1
    else:
        seat.append(S[i])
print(cnt)
print(seat)