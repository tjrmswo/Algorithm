# 1번은 공백, AC를 치려면 p초 입력 w초 기다리고 p*3
p, w = map(int, input().split())
S = list(input())
lst = {{1: ''}, {2: ['A', 'B', 'C']}, {3: ['D', 'E', 'F']},
       {4: ['G', 'H', 'I']}, {5: ['J', 'K', 'L']}, {6: ['M', 'N', 'O']}
    , {7: ['P', 'Q', 'R', 'S']}, {8: ['T', 'U', 'V']}, {9: ['W', 'X', 'Y', 'Z']}}
result = 0
check = 0
for i in range(len(S)):
    print(i)
