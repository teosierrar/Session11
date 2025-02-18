from itertools import count

import requests

book = requests.get('https://www.gutenberg.org/cache/epub/1513/pg1513.txt')
print(book.text)
lines = book.text.split('\n')
punctuation_remove = ",.!?:;"
punctuation_space = "',\()[]=-+_"
unique_words = {}

for line in lines:
    # replace punctuation
    for c in punctuation_remove:
        line = line.replace(c, " ")
    for c in punctuation_space:
        line = line.replace(c, " ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words[word] = unique_words.get(word, 0) + 1

print(unique_words)
print(len(unique_words))
