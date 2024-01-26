A = [1,2]
B = [3,4]
def solution(A, B):
    A, B = sorted(A), sorted(B,reverse=True)
    return sum([A[i] * B[i] for i in range(len(A))])
print(solution(A,B))