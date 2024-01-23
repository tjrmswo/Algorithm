n = 10

# def solution(n):
#     answer = 0
#     for i in range(2,n+1):
#         for j in range(2,int(i**(0.5)) + 1):
#             if i % j == 0:
#                 break
#         else:
#             answer += 1
#     return answer

def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
            print('for in num:', num)

    return len(num)


print(solution(n))
