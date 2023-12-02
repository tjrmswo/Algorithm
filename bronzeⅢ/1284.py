# 각 숫자 사이 에는 1cm의 여백이 들어 가야 한다.
# 1은 2cm의 너비를 차지 해야 한다. 0은 4cm의 너비를 차지 해야 한다.
# 나머지 숫자는 모두 3cm의 너비를 차지 한다.
# 호수 판의 경계와 숫자 사이 에는 1cm의 여백이 들어 가야 한다.

while 1:
    N = input()
    if N == '0':
        break
    cnt = len(N)+1
    for n in N:
        if n == '0':
            cnt += 4
        elif n == '1':
            cnt += 2
        else:
            cnt += 3
    print(cnt)