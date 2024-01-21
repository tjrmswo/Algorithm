a,b,n = 3,1,20
# def solution(a, b, n):
#     result = 0
#
#     if n % a != 0:
#         result += n % a
#
#     if n <= 1:
#         return (n + result) // a if result != 0 else n
#
#     return n // a + solution(a, b, n // a)
def solution(a, b, n):
    answer = 0
    # 가지고 있는 콜라병이 교환 가능한 동안에
    while n >= a:
        # 빈 병 개수 추가
        answer += (n // a * b)
        # 교환하지 못하고 남은 병 + 새로 얻은 콜라
        n = (n % a) + (n // a * b)
    return answer
print(solution(a,b,n))