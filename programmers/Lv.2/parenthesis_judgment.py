# ()() or (())()와 같이 괄호가 올바르게 닫혀있는지 판단하라

# 올바른 조건은 (의 개수와 )의 개수가 맞고 (())))( 와 같지 않아야 함
# 개수가 맞고, (이 )보다 뒤에 있으면 안 됌 (())()와 같은 경우는 가능
s = '((()))('
# def solution(s): # 90.5점
#     answer = True
#     left = 0
#     right = 0
#     for i in range(len(list(s))):
#         if s[i] == '(':
#             left += 1
#             last_left = i
#         else:
#             right += 1
#             last_right = i
#         if left == right and last_left < last_right:
#             answer = True
#         else:
#             answer = False
#     return answer

def solution(s):
    stack = []
    for i in s:
        if i == '(':  # '('는 stack에 추가
            stack.append(i)
        else:  # i == ')'인 경우
            if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
                return False
            else:
                stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거
        print(stack)
    return stack == []
print(solution(s))
