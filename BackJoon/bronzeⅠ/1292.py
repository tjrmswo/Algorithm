# 1은 한 번 N은 N번 수열 1223334444 을 만들고 일정 구간을 주면 그 구간의 합을 구하는 것
# 첫째 줄에 구간의 시작과 끝을 나타 내는 정수 A,B가 주어짐.
# 즉, 수열 에서 A번째 숫자 부터 B째 숫자 까지 합을 구하면 됌
# 1223334444555556666667777777
# 1 2 3   4   5    6      7

N,M = map(int,input().split())
cnt = [0]
for i in range(46):
    for j in range(i):
        cnt.append(i)
print(sum(cnt[N:M+1]))
