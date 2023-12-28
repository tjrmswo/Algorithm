N = int(input())
list_value = list(map(int,input().split()))
cnt = []
a = 0
for i in range(N-1):
    if list_value[i] < list_value[i+1]:
        a += list_value[i+1] - list_value[i]
    else:
        cnt.append(a)
        a = 0
cnt.append(a)
print(cnt)