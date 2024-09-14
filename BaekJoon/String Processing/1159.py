# 성의 첫 글자가 같은 선수 5명을 선발 하려고 한다.
# 성의 첫 글자가 같은 선수가 5명보다 적다면 친선 경기를 기권
# 뽑을 수 있는 성의 첫 글자를 모두 구하기
# babic arr[1]
# keksic arr[2] 다르면 앞,뒷 부분 1증가
# boric arr[2] == arr[3] 앞 뒤 부분 1 증가
# bukic arr[3] == arr[4] 다르면 뒤만 1증가
# sarmic arr[3] == arr[5]
# balic
# kruzic
# hrenovkic
# beslic
# boksic
# krafnic
n = int(input())
player_list = []
result = []

for _ in range(n):
    a = input()
    player_list.append(a[0])

first_names = set(player_list)

for i in first_names:
    if player_list.count(i) >= 5:
        result.append(i)

if len(result) > 0:
    print(''.join(sorted(result)))
else:
    print("PREDAJA")
