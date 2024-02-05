#세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
# 150
# 266
# 427
numbers = [0,1,2,3,4,5,6,7,8,9]
arr = []
result = 0
for i in range(3):
    N = int(input())
    arr.append(N)
N = arr[0]*arr[1]*arr[2]
list_N = list(map(int,str(N)))
for i in numbers:
    print(list_N.count(i))