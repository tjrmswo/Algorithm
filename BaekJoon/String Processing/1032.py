N = int(input())
first_word = list(input())
first_word_len = len(first_word)

for _ in range(N-1):
    other_word = list(input())
    for j in range(first_word_len):
        if first_word[j] != other_word[j]:
            first_word[j] = "?"
print(''.join(first_word))
