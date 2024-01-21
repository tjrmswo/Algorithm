strings = ["abce", "abcd", "cdx"]
n = 2
# def solution(strings, n):
#     answer = []
#     result = {}
#     for i in range(len(strings)):
#         result[i] = strings[i]
#         result = dict(sorted(result.items(), key=lambda x:x[1][n]))
#
#     print(result)
#     return answer
def solution(strings, n):
    strings.sort()
    print(strings)
    return sorted(strings, key=lambda x:x[n])

print(solution(strings,n))