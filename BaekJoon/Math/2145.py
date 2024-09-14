# 주어진 숫자의 각 자릿 수를 더한다.
# 결과가 한 자릿 수가 될 때 까지 규칙1을 반복 한다.

while True:
    N = input()
    if int(N) == 0:
        break
    while int(N) > 9:
        N = sum(map(int,list(str(N))))
    print(N)

