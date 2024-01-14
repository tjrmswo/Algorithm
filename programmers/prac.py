N,n = input().split()
def solution(my_string, is_prefix):
    answer = 0
    for i in range(0,len(my_string)):
        my_string = my_string[:i]
        if my_string == is_prefix:
            answer = 1
            break
        else:
            continue
    print(answer)
    return answer
solution(N,n)

