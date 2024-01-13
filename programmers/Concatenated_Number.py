numlist = list(input().split())
def solution(num_list):
    odd_result = ''
    even_result = ''
    for i in range(len(num_list)):
        if int(i) % 2 == 0:
            even_result += num_list[i]
            print(even_result)
        elif int(i) % 2 == 1:
            odd_result += num_list[i]
            print(odd_result)
    answer = int(odd_result) + int(even_result)
    print(answer)
    return answer
solution(numlist)