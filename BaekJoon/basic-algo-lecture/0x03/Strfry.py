# strfry함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어낸다
# 두 개의 문자열에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여
# 얻어질 수 있는지 판단
N = int(input())
result = []
for _ in range(N):
    S1, S2 = map(str, input().split())
    result.append([S1, S2])

for i in range(len(result)):
    S1 = sorted(result[i][0])
    S2 = sorted(result[i][1])
    if S1 == S2:
        print("Possible")
    else:
        print("Impossible")
