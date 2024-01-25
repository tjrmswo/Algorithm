babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa",'mama','woowoo']


def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']

    for bab in babbling:  # babbling의 단어 하나씩 확인
        print("bab: ",bab)
        for c in can:
            print("c:",c)
            if c * 2 not in bab:  # 연속으로 나오지 않으면 공백(' ')으로 대체
                bab = bab.replace(c, ' ')
        print("for after bab: ", bab)
        if bab.isspace():  # 공백으로만 이루어져 있으면 answer+1
            answer += 1

    return answer
# def solution(babbling):
#     baby_cansay = ['aya', 'ye', 'woo', 'ma']  # 아기가 말할 수 있는 단어 배열
#     result = []  # 결과를 담을 배열
#     before_say = ''  # 방금 전 아기가 말한 단어
#
#     for i in range(len(babbling)):
#         saying = babbling[i]
#         for j in range(len(babbling[i])):
#             if before_say == babbling[i][j]:
#                 continue
#             before_say += babbling[i][j]  # aya
#             print('saying', saying, 'before_say', before_say)
#             if before_say in baby_cansay:
#                 saying = saying.replace(before_say, '')  # aya ,''
#                 print('replace_saying:', saying)
#                 before_say = ''
#                 if saying == '':
#                     result.append(babbling[i])
#                     print('append_result: ', result)
#                     break
#         before_say = ''
#     print(result)
    return len(result)


print(solution(babbling))
