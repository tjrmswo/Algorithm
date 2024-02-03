
lottos = [0, 0, 0, 0, 0, 0]
win = [31, 10, 45, 1, 6, 19]
# def solution(lottos, win_nums):
#     answer = []
#     result = 0
#     zero = 0
#     for i in range(len(win_nums)):
#         print("lottos[i]: ",lottos[i])
#         if lottos[i] in win_nums:
#             result += 1
#             print('result',result)
#         elif lottos[i] == 0:
#             zero += 1
#             print("zero",zero)
#     if zero == 6:
#         answer.append(7 - (result + zero))  # 최고 순위
#         answer.append(zero)  # 최저 순위
#     else:
#         answer.append(7 - (result + zero))  # 최고 순위
#         answer.append(7 - result)  # 최저 순위
#     return answer
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
print(solution(lottos,win))