# 하나의 플러그 N개의 멀티탭이 있음. 각 멀티탭은 몇 개의 플러그로 이루어져있음
# 최대 몇 대의 컴퓨터를 전원에 연결할 수 있을까?

# 3 1 1 1 => 1개 왜냐면 멀티탭 3개지만 1개의 플러그들로 이루어져 있으므로.
# 2 5 8은 => 12개 왜냐면 첫번째 멀티탭에 두번째를 연결해야 하고 나머지 멀티탭의 개수를 세면 12개임
# 4 1 3 1 2 => 5개
# 3 2 1 6 => 1 0 6 => 7
# 3 5 8 3 => 14
import sys

num = int(sys.stdin.readline())
sum = 1
for i in range(num):
    tempNum = int(sys.stdin.readline())
    sum+=tempNum

print(sum-num)
