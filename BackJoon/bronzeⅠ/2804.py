# 크로스워드 퍼즐
# 두 단어 A와 B가 주어짐. A는 가로로 놓이고 B는 세로로 놓여야 함
# 두 단어는 서로 교차해야 함. 정확히 한 글자를 공유해야함

# 배열이 시작할 row 값과 column 값을 구하고 2차원 배열을 통해
# 해당 인덱스에만 문자를 추가한다.
M,N = list(input().split())

for i in range(len(M)):
    if M[i] in N:
        col = i
        row = N.index(M[i])
        break

for i in range(len(N)):
    if i == row:
        print(M)
    else:
        print("."*col + N[i] + '.'*(len(M)-col-1))

