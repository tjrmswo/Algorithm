# N개의 A,G,C,T로 구성되어 있는 DNA 암기 서열이 있음.
# 해독 방법은 염기 서열에서 제일 끝에 있는 두 개의 염기를 An-1, An이라 할 때ㅡ
# An-1 행으로 An을 열로 대응시켜 그에 해당하는 하나의 염기를 바꾸는 방식으로 반복
# AAGTCG라는 염기서열이 있다고 하면, AAGTCG > AAGTT > AAGT > AAA > AA > A 가 됌.

N = int(input())
S = list(input())
dna = {"AA" : "A", "AG" : "C", "AC" : "A", "AT" : "G", "GA" : "C","GG" : "G",
       "GC" : "T", "GT" : "A", "CA" : "A", "CG" : "T", "CC" : "C", "CT" : "G",
       "TA" : "G", "TG" : "A", "TC" : "G","TT" : "T"}

while True:
    if len(S)==1:
        break
    ss=S[-2]+S[-1]
    if ss in dna:
        del S[-2:]
        S.append(dna.get(ss))
print(''.join(S))

# 둘의 염기 서열이 같으면 그대로 출력 4개 해결
# 같은 염기 서열을 포함하면 같은 값이 나옴 예 AG, GA = C 나머지는 이런 규칙
# 둘 다 바꿀 필요 없이 맨 마지막 자릿 수는 버리고 그 다음 자릿수는 알맞은 알파벳으로 바꾸어
# 주면 됌