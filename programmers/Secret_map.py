n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
def solution(n, arr1, arr2):
    answer = []
    result = ''
    for one, two in zip(arr1,arr2):
        one = list(bin(one)[2:].zfill(n))
        two = list(bin(two)[2:].zfill(n))
        for i in range(len(two)):
            if one[i] == '1' or two[i] == '1':
                result += "#"
            else:
                result += " "
        answer.append(result)
        result = ''
    return answer
print(solution(n,arr1,arr2))