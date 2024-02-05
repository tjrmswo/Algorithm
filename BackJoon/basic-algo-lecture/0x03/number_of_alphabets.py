# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s = list(input().lower())
result = [0]*26
for i in s:
    index = arr.index(i)
    result[index] += 1
print(' '.join(map(str, result)))
