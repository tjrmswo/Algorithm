N = int(input())
list_value = []
for i in range(N):
    value = list(map(int, input().split()))
    list_value.append(sorted(value))

for i in range(N):
    print(list_value[i][-3])