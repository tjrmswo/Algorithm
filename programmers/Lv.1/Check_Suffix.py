M, S = input().split()
def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if my_string == is_suffix:
            answer = 1
            break
        else:
            my_string = my_string[1:]
            if len(my_string) == 0 :
                answer = 0
    print(answer)
    return answer
solution(M,S)
