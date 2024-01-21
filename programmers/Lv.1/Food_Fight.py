#  칼로리가 낮은 음식을 먼저 먹을 수 있게 배치하여 선수들이 음식을 더 잘 먹을 수 있음
#  1번 2개 ,2번 4개 , 3번 6개
# [0,111,2222,333333]
N = list(map(int,input().split()))
def solution(food):
    temp = '' # 왼쪽 선수 음식
    for i in range(1, len(food)):
        temp += str(i) * (food[i]//2)
    return temp + '0' + temp[::-1]
print(solution(N))