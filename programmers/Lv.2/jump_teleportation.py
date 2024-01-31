# k칸을 앞으로 점프하거나, 현재까지 온 거리 x 2에 해당하는 위치로 순간이동을 할 수 있는
# 특수한 기능을 가진 아이언 슈트를 개발
# 점프하면 k만큼 건전지 사용량이 듬
# N만큼 떨어져 있는 장소로 가려고 함 N이 주어졌을 때 건전지 사용량의 최솟값을 return

N = 6
def solution(n):
    ans = 0
    for i in range(n):
        if n % 2 == 1:
            ans += 1
            n -= 1
        elif n == 0:
            break
        n = n // 2
    return ans
# 2500 1250 625 624 312 156 78 39 38 19 18 9 8 4 2 1 0
# 5 4 2 1 0
print(solution(N))