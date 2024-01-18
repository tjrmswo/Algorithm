S = "one4seveneight"
# numbers = ['zero', "one", "two", "three", "four","five","six","seven","eight","nine"]
# def solution(s):
#     answer = 0
#     for i in range(len(numbers)):
#         if numbers[i] in s:
#             s = s.replace(numbers[i],str(i))
#     return answer

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)



solution(S)
