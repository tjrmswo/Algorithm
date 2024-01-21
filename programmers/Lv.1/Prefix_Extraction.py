N,n = input().split()
def solution(my_string, is_prefix):
    answer = 0
    prefix = ''
    for i in range(len(my_string)):
        prefix += my_string[i]
        if prefix == is_prefix:
            answer = 1
            break
        else:
            continue
    return answer
solution(N,n)