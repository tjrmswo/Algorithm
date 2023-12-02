# 3개의 주사위를 던져 규칙에 따라 상금을 받는 게임
# 같은 눈 3개 = 10000원+ 같은 눈 x 1000원
# 같은 눈 2개 = 1000원+ 같은 눈 x 100원
# 모두 다른 눈 가장 큰눈 x 100원

N = int(input())
arr = []
for i in range(0,N):
    A, B, C = map(int,input().split())
    conts = max(A,B,C)
    if A == B and A == C :
        arr.append(10000+conts*1000)
    elif (A == B and A != C) or (A != B and A == C) or (B == C and A != C):
        arr.append(1000+conts*100)
    elif A != B != C:
        arr.append(conts*100)
    else:
        print("값을 확인해주세요")
print(max(arr))