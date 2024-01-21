k = 3
m = 4
score = [1,2,3,1,2,3,1]
def solution(k, m, score):
    answer = 0
    result = []
    score = sorted(score,reverse=True)
    for i in range(len(score)):
        result.append(score[i])
        print("result",result)
        if len(result) == m:
            answer += min(result) * m
            result = []
    return answer
print(solution(k,m,score))
