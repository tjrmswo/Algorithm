weeks = ['THU','FRI','SAT','SUN','MON','TUE','WED']
days = [31,29,31,30,31,30,31,31,30,31,30,31]
a = 5
b = 24
def solution(a, b):
    answer = ''
    result = b
    for i in range(len(days)):
        if i == (a-1):
            break
        result += days[i]
    print(weeks[result % 7])
    return answer
solution(a,b)