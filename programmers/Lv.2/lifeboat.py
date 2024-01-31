# 최대 2명, 무게 제한 있음
# 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면
# 2 4번은 같이 탈 수 있지만 , 1 3은 같이 못 탐
# 구명 보트를 최대한 적게 사용하여 모든 사람을 구출하려고 함
# 사람의 몸무게를 담은 배열 people과 구명보트의 무게 제헌 limit가 매개변수로 주어지면
# 구명보트의 개수의 최솟값을 return
people = [70, 50, 80,50]
limit = 100


# 70+80 150  2
def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        print("people[b]: ", people[b], 'people[a] : ',people[a], b)
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


print(solution(people, limit))
