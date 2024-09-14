# 0 ~ 9번까지 숫자가 하나씩 들어가 있음 다솜이의 방 번호가 주어졌을 때, 필요한
# 세트의 개수의 최솟값을 출력 6과 9는 서로 뒤집어서 이용 가능

# 6과 9가 없는 숫자들은 max 함수 만드로도 충분함 하지만 6과 9가 있다면
N = list(map(int, input()))
numbers = [0] * 10
for i in N:
    numbers[i] += 1

sixnine = (numbers[6] + numbers[9] + 1) // 2
numbers[6] = sixnine
numbers[9] = sixnine
print(max(numbers))
# print(numbers)
# print(sixnine)

# 평소 로직은 12635 => 자릿수가 모두 다르기 때문에 1개의 세트로 충분
# 6이나 9는 뒤집어서 사용이 가능해 그래서 이럴 때는 6과 9의 개수를 //으로 나누고 +1을 해줘야 함
# 그렇다면 22423과 같은 경우에는 2가 3개니까 가장 많은 요소의 갯수가 곧 필요한 세트의 개수

# 9999
# 2
# 122
# 2
# 12635
# 1
# 888888
# 6
