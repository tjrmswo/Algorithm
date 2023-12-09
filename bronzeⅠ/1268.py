# 서로 같은 반이였던 사람이 많은 학생을 임시반장으로 선출하려고 함
# 임시 반장으로 정해진 학생의 번호를 출력하는데 여러 명인 경우에 가장 작은 번호만 출력

N = int(input())
students = []
for i in range(N):
    students.append([int(j) for j in input().split()])

max_friend = -1
banjang = -1
for student_no in range(N):
    result = set()
    for grade in range(5):
        for friend in range(N):
            if students[student_no][grade] == students[friend][grade]:
                result.add(friend)

    if len(result) > max_friend:
        banjang = student_no + 1
        max_friend = len(result)