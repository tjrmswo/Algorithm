# A,B = input().split()
# cnt = 0
# for i in A:
#     for j in B:
#         cnt += int(i)*int(j)
# print(cnt)

import sys
input = sys.stdin.readline()

A,B = map(list,input.split())
print(A,B)
A = list(map(int,A))
B = list(map(int,B))
print(A,B)
print(sum(A)*sum(B))