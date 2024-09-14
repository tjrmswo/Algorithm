# Rev(x)는 모든 수를 뒤집은 수다. X = 100이면 Rev(100) = 1인 셈
# x와 y가 주어졌을 때 Rev(Rev(x)+Rev(y))를 구해라

# X,Y = input().split()
#
# def reverseNumber(n):
#     res = ''
#     for i in n:
#         if i == '0':
#             continue
#         else:
#             res += i
#     return int(res)
# one = reverseNumber(X[::-1]) + reverseNumber(Y[::-1])
# two = reverseNumber(str(one))
# reverseResult = str(two)[::-1]
# print(reverseResult)

a,b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(int(str(a+b)[::-1]))
print(str(a+b)[::-1])
print(int(str(a+b)[::-1]))