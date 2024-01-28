# n명이 끝말잇기중, 규칙은 1번부터 번호 순서대로 한 사람씩 단어를 말함
# 마지막 사람이 단어를 말하면 다시 1번부터
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 함
# 이전에 등장했던 단어는 사용 x, 한 글자인 단어는 인정 x
# 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째에 차례에 탈락하는지 구해서 return
n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]


def solution(n, words):
    answer = []
    duplicate_words = []
    duplicate_words.append(words[0])
    for i in range(1, len(words)):
        last_word = words[i - 1][-1:]
        first_word = words[i][:1]
        duplicate_words.append(words[i])
        print("last_word:", last_word, "first_word: ", first_word)
        print('i: ', words[i])
        print(duplicate_words)
        if last_word != first_word:
            answer.append((i % n)+1)
            answer.append((i // n)+1)
        else:
            if duplicate_words.count(words[i]) > 1:
                answer.append((i % n)+1)
                answer.append((i // n)+1)
    if len(answer) == 0:
        answer = [0,0]
    return answer


print(solution(n, words))
