# cnt = 0
# for i in range(0,3):
#     S = input()
#     if i == 0:
#         if S == 'black':
#             cnt += 0
#         elif S == 'brown':
#             cnt += 10*1
#         elif S == 'red':
#             cnt += 10*2
#         elif S == 'orange':
#             cnt += 10*3
#         elif S == 'yellow':
#             cnt += 10*4
#         elif S == 'green':
#             cnt += 10*5
#         elif S == 'blue':
#             cnt += 10*6
#         elif S == 'violet':
#             cnt += 10*7
#         elif S == 'grey':
#             cnt += 10*8
#         elif S == 'white':
#             cnt += 10*9
#     if i == 1:
#         if S == 'black':
#             cnt += 0
#         elif S == 'brown':
#             cnt += 1
#         elif S == 'red':
#             cnt += 2
#         elif S == 'orange':
#             cnt += 3
#         elif S == 'yellow':
#             cnt += 4
#         elif S == 'green':
#             cnt += 5
#         elif S == 'blue':
#             cnt += 6
#         elif S == 'violet':
#             cnt += 7
#         elif S == 'grey':
#             cnt += 8
#         elif S == 'white':
#             cnt += 9
#     elif i == 2:
#         if S == 'black':
#             cnt *= 1
#         elif S == 'brown':
#             cnt *= 10
#         elif S == 'red':
#             cnt *= 100
#         elif S == 'orange':
#             cnt *= 1000
#         elif S == 'yellow':
#             cnt *= 10000
#         elif S == 'green':
#             cnt *= 100000
#         elif S == 'blue':
#             cnt *= 1000000
#         elif S == 'violet':
#             cnt *= 10000000
#         elif S == 'grey':
#             cnt *= 100000000
#         elif S == 'white':
#             cnt *= 1000000000
# print(cnt)

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
N = str(color.index(input()))
M = str(color.index(input()))
O = str(10**color.index(input()))
print(N+M+O[1:])