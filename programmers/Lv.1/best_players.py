k = 3
score = [10, 100, 20, 150, 1, 100, 200]


def solution(k, score):
    answer = []
    result = []
    for i in range(len(score)):
        result.append(score[i])
        result = sorted(result,reverse=True)
        if len(result) < k:
            answer.append(result[-1])
        else:
            answer.append(result[k-1])
        print("answer",answer)
    return answer


solution(k, score)
