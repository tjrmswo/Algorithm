N = list(map(int,input().split()))
def solution(num_list):
    mul = 1
    power = 0
    for i in num_list:
        print(i)
        mul *= i
        power += i
    power = power**2
    print(mul)
    print(power)
    if mul < power:
        answer = 1
    else:
        answer = 0
    return answer
solution(N)
