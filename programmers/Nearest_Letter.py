N = "banana"
def solution(s):
    answer = []
    last_pos = {}  # 각 문자의 마지막 위치를 저장하는 딕셔너리

    for i, char in enumerate(s):
        if char in last_pos:  # 이미 같은 문자가 앞에 나왔다면
            answer.append(i - last_pos[char])  # 현재 위치와 저장된 위치의 차이를 결과에 추가
        else:  # 처음 나온 문자라면
            answer.append(-1)  # -1을 결과에 추가
        last_pos[char] = i  # 현재 문자의 위치를 저장
        print(last_pos)
    return answer
print(solution(N))