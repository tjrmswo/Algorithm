#   4 * 1 2*1-1  2*i-1
#  3 *** 3 2*2-1
# 2 ***** 5 2*3-1
#1 ******* 7 2*4-1
# ********* 9 2*5-1
#  ******* 7 6 2*4-1 2*5-5+1 1
#   ***** 5 7 2*3-1 2
#    *** 3 8 2*2-1 3
#     * 1 9 2*1-1 4
N = int(input())
for i in range(1, N):
    print(' ' * (N - i) + '*' * (2 * i - 1))
for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))