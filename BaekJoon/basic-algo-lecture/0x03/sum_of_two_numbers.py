# 서로 다른 양의 정수 a~an으로 이루어진 수열
# 자연수 x가 주어졌을 때, b+c = x를 만족하는
# (b,c)쌍의 수를 구하는 프로그램을 구하시오
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
result = 0

arr_set = set(arr)

for num in arr:
    complement = x - num
    if complement in arr_set:
        result += 1

print(result // 2)
# 9
# 5 12 7 10 9 1 2 3 11
# 13

# Two Point Algorithm
# start = 0
# end = len(arr) - 1
# for i in range(len(arr)):
#     start = 0
#     while start < end:
#         if arr[start] + arr[end] != x:
#             start += 1
#         else:
#             result += 1
#             break
#     end -= 1


