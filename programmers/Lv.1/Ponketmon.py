nums = [3,1,2,3]
def solution(nums):
    answer = set(map(str,nums))
    print(answer)
    print(round(1.5))
    return round(len(set(map(str,nums)))//2)
print(solution(nums))