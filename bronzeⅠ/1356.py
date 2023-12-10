# 어떤 수를 10진수로 표현한 뒤 그 수를 두 부분으로 나눴을 때
# 앞 부분 자리 수의 곱과 뒤수분 자리수의 곱이 같을 때를 말함.

def mul(s):
    res = 1
    for c in s:
        res *= int(c)
    return res


n = input()

check = False
for i in range(1, len(n)):
    s1 = n[:i]
    s2 = n[i:]
    res1 = mul(s1)
    res2 = mul(s2)
    if res1 == res2:
        check = True
        break

if check == True:
    print("YES")
else:
    print("NO")

