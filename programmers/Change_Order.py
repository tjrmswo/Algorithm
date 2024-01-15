N = list(map(int,input().split()))
n = int(input())
def solution(num_list, n):
    answer = []
    answer.extend(num_list[n:])
    num_list = num_list[:n]
    answer.extend(num_list)
    print(answer)
    return answer
solution(N,n)