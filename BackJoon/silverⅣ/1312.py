N , M, O = map(int,input().split())
for i in range(O):
    N = (N%M) * 10
    result = N//M
print(result)




