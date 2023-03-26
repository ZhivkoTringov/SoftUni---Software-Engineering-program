from collections import defaultdict

words= input().split(' ')
counter = defaultdict(int)
for word in words:
    counter[word.lower()] += 1
print(' '.join([word for word, count in counter.items() if count % 2 != 0]))

