n = 15


def solution(n):
    answer = 0
    bin_n = bin(n)[2:]
    n_one = 0
    for i in str(bin_n):
        if i == '1':
            n_one += 1
    while True:
        n += 1
        next_n = bin(n)[2:]
        one = 0
        for i in str(next_n):
            if i == '1':
                one += 1
        if one == n_one:
            answer = n
            break
    return answer
print(solution(n))