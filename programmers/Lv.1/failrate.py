N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):  # 실패율 O(n)
    sum_list = [0] * (N + 2)
    dic_list = {}
    stages.sort()
    print("stages.sort()",stages)
    now = len(stages)
    for i in stages:
        sum_list[i] += 1
    print('각 스테이지에 도달한 사람의 수: ',sum_list)
    for i in range(1, N + 1):
        if now == 0:
            dic_list[i] = 0
            continue
        dic_list[i] = sum_list[i] / now
        print("dic_list: ",dic_list)
        now -= sum_list[i]
    return sorted(dic_list, key=lambda x: dic_list[x], reverse=True)
print(solution(N,stages))