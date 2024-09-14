# 메세지 암호화
# 만드는 방법은 문자열을 1,1부터 아래 순서대로 채운다.
# 그리고 가장 밑의 행을 채운 후에 오른쪽 열에서 다시 같은
# 과정을 반복. 암호화 된 문자열과 몇 개의 열로 암호화를 하였는지
# 주어져 있을 때 원래의 문자열을 구하는 프로그램
# import math
# N = int(input())
# S = list(input())
# cnt = []
# divided = math.ceil(len(S) / N)
# s = ""
# for i in range(divided):
#     cnt.append(sorted(S[:N]))
#     S = S[N:]
#     print('cnt', cnt,len(cnt))
#     print("S: ",S)
#
# for i in range(N):
#     for j in range(divided):
#         s += cnt[j][i]
# print(s)

from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()
arr = []
for i in range(0, len(s), n):
    arr.append(list(s[i:i+n]))

for i in range(len(arr)):
    if i % 2 != 0:
        data = list(reversed(arr[i]))
        arr[i] = data

res = ''
for j in range(n):
    for i in range(len(arr)):
        res += arr[i][j]
print(res)