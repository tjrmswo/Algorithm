n = 15


def solution(n):
    answer = 0
    for i in range(1,n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
    return answer

# def solution(n):
#     return len([i for i in range(1, n + 1, 2) if n % i == 0])


print(solution(n))
