nums = [1, 2, 3, 4]


def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):

                result = nums[i] + nums[j] + nums[k]

                for j in range(2, result):
                    if i % j == 0:
                        break
                else:
                    answer += 1
    return answer


print(solution(nums))
