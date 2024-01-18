Ns = 32142123
N = 'pPoooyY'
n = [3,2,13]
m = [1,8,76]
def solution(n):
    if n < 10:
        return [n]
    return [n % 10] + solution(n // 10)
print(solution(Ns))
print(n+m)
print(sorted(n,reverse=True))
