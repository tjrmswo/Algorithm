# 다트 3개를 던짐 0~10점까지 있고 Single(S), Double(D), Triple(T) 1제곱, 2제곱, 3제곱으로 계산
# 옵션으로 스타상(*), 아차상(#)이 존재하는데 스타상 당첨되는 해당 점수와 바로 전에 얻은 점수를
# 각 2배, 아차상 당첨은 해당 점수 마이너스
# 스타상은 첫번째 나오게 되면 스타상의 점수만 2배, 스타상의 효과는 중첩될 수 있고,
# 중첩된 스타상의 점수는 4배가 됌
# 스타상의 효과는 아차상의 효과와 중첩될 수 있음 중첩된 아차상의 점수는 -2배
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다
# 스타상 아차상은 점수마다 둘 중 하나만 존재, 존재하지 않을 수도 있음
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성
dartResult = '1S2D*3T'


def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1

    return sum(score)


print(solution(dartResult))

