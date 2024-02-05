# 0 ~ 9번까지 숫자가 하나씩 들어가 있음 다솜이의 방 번호가 주어졌을 때, 필요한
# 세트의 개수의 최솟값을 출력 6과 9는 서로 뒤집어서 이용 가능

# 6과 9가 없는 숫자들은 max 함수 만드로도 충분함 하지만 6과 9가 있다면
N = list(map(int,input()))
result = []
sixAndnine = 0
for i in N:
    if i == 6 or i == 9:
        sixAndnine += 1
        result.append(sixAndnine // 2)
    else:
        result.append(N.count(i))
print(result)
print(sum(result))