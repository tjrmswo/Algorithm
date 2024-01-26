s = "3people unFollowed me"
def solution(s):
    answer = ''
    s = s.lower()
    words = s.split(' ')
    print(words)
    for word in words:
        if word:
            answer += word[0].upper() + word[1:]
        answer += ' '
    return answer[:-1]

print(solution(s))