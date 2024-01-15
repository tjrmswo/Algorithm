Ns = "oxooxoxxox"
def solution(myString):
    answer = []
    result = 0
    for i in range(len(myString)):
        if myString[i] != 'x':
            answer.append(myString[i])
        # elif myString[i] == 'x':
        #     answer.append(result)
        #     result = 0
    print(answer)
    print(len(myString))
    return answer
solution(Ns)
