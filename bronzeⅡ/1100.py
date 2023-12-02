# 0,0 2,0 4,0 6,0 규칙 발생 y가 홀수면 홀수칸 짝수면 짝수칸이 흰색이다.
# 1,1 3,1 5,1 7,1
# 0,2 2,2 4,2 6,2
# .F.F...F [0]1[2]3[4]5[6]7
# F...F.F.
# ...F.F.F
# F.F...F.
# .F...F..
# F...F.F.
# .F.F.F.F
# ..FF..F.
cnt = 0
for i in range(8):
    S = input()
    if i % 2 == 0:
        a=S[::2]
        cnt += a.count('F')
    elif i % 2 == 1:
        b=S[1:8:2]
        cnt += b.count('F')
print(cnt)