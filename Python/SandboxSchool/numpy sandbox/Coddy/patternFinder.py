def find_occurrences(text, pattern):
    text.count(pattern)


text = input()
pattern = input()


result = find_occurrences(text, pattern)
print(result)