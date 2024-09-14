# 금민수는 4와 7로 이루어진 수인데 N보다 작거나 같은 금민수 중 가장 큰 것을
# 출력하는 프로그램 작성
N = int(input())
while True:
    cnt = True
    for i in str(N):
        if i != "4" and i != "7":
            cnt = False
            N -= 1
    print(N)
    if cnt :
        print(N)
        break


