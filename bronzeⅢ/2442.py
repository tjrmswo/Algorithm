#     *
#    ***
#   *****
#  *******
# *********
# 1 3 5 7 9
N = int(input())
for i in range(1,N+1):
    print(" "*(N-i)+"*"*(2*i-1))