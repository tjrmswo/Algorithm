def max_score(stairs):
    n = len(stairs)
    if n == 0:
        return 0
    if n == 1:
        return stairs[0]
    if n == 2:
        return stairs[0] + stairs[1]

    # dp 배열 초기화
    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    # dp 테이블 채우기
    for i in range(3, n):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    return dp[n-1]

# 프로그램 실행 예제
import sys

input = sys.stdin.readline
n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]

print(max_score(stairs))