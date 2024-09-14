
# 12321 이것은 i[0] = i[4] i[1] = i[3]
# 121 i[0] = i[2]
# 154676451 i[0] = i[8] i[1] = i[7] 2 = 6 3 = 5 4
while True:
    S = input()
    if S == '0':
        break
    if S == S[::-1]:
        print('yes')
    else:
        print('no')
