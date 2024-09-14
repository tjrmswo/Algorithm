T = int(input())
power = 0
for i in range(T):
    N = int(input())
    res = len(str(N))
    if str(N**2)[-res:] == str(N):
        print("YES")
    else:
        print("NO")