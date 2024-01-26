x = "110010101001"


def solution(s):
    answer = []
    zero = 0
    binary_conversion = 0
    while True:
        if s == '1':
            break
        for i in s:
            if i == '0':
                zero += 1
        s = bin(len(s.replace("0", '')))[2:]
        binary_conversion += 1
    answer.append(binary_conversion)
    answer.append(zero)
    return answer
print(solution(x))
