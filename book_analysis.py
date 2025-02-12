book=requests.get("https://www.gutenberg.org/cache/epub/345/pg345.txt")



import
print(book.text)
lines=book.text.split('\n')
punctuation_remove=",.!?;"
punctuation_space="'\"()[]=-_"
for lines in lines:
    for c in punctuation_remove:
        line=line.replace(c,"")
    for c in punctuation_space:
        line=line.replace(c," ")
    print(line)