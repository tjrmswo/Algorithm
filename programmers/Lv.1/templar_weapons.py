# 기사는 1번부터 number까지 번호가 지정됌
# 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기를 구매하려함
# 제한수치보다 큰 무기를 사야하는 사람은 정해진 공격력을 가진 무기가 주어짐
# 1,3,5,15 4개 이므로 공격력이 4인 무기 구매
# 제한 수치가 3이고 제한수치를 초과한 기사가 사용할 무기 공격력이 2라면 공격력이 2인 무기 구매
# 공격력 1당 1kg의 철이 필요하고 무기를 모두 만들기 위해 필요한 철의 무게를 계산하라.

number = 20
limit = 8
power = 2

# def solution(number, limit, power):
#     answer = 1
#     measure = [1]
#     for i in range(2,number+1):
#         for j in range(2, i+1):
#             if i % j == 0:
#                 answer += 1
#         if answer > limit:
#             measure.append(power)
#         else:
#             measure.append(answer)
#         answer = 1
#     print(measure)
#     answer = sum(measure)
#     return answer
def solution(number, limit, power):
    divisors = []                             # 약수 list
    for i in range(1, number+1):              # 1부터 number까지 for loop
        divisor = 0
        for j in range(1, int(i**(1/2)) + 1): # 1부터 i의 제곱근까지 for loop
            if i % j == 0:
                divisor += 1
                if j**2 != i:                 # 제곱이 되는 수는 count 1을 하여 중복 방지.
                    divisor += 1
            if divisor > limit:               # limit값을 초과하면 power값으로 return
                divisor = power
                break
        divisors.append(divisor)
    return sum(divisors)
print(solution(number,limit,power))