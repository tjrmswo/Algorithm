# 단어의 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램
# 관계에 있다고 한다. 두 개의 영단어가 중졌을 때, 두 단어가 서로 애너그램 관계에 있도록
# 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램 작성

# 애너그램 관계에 있을 때 판별법이 있나..?
# 일단 방법1 정렬된 s와 y를 탐색한다.
s = list(input())
y = list(input())
s1, y1 = s[:], y[:]
s2 = []
for x in s:
    print("x: ",x)
    if not x in y1 or y1.remove(x):
        print(x)
out1 = [x for x in s if not x in y1 or y1.remove(x)]
out2 = [x for x in y if not x in s1 or s1.remove(x)]
# vvbbccs
# bbcsaaa
print(len(out1)+len(out2))
