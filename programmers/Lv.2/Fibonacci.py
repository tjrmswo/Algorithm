# 피보나치 수 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2)가
# 적용되는 수
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수
n = 5

#
# def solution(n):
#     F0, F1 = 0, 1
#     result = [0]
#     for i in range(1,n+1):
#         if i == 2:
#             result.append(F0 + F1)
#             print("i == 2:",result)
#         elif i == 1:
#             result.append(F1)
#             print("i == 1: ",result)
#         else:
#             result.append(result[i-2] + result[i-1])
#             print("others:",result)
#     return result[n] % 1234567
# print(solution(n))
def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a+b
        print('i:',i,"a:",a,"b:",b)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(5))


