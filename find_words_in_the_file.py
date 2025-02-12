punctuation_remove=(",.!?")
punctuation_space=("'")

def find_3_letter_words(filename):
    """
    Finds all the 3 letter words
    :param filename: The file we are using
    :return: The words with three letters starting with b or B
    """
    with open(filename) as f:
        for line in f:
            for p in punctuation_remove:
                line=line.replace(p,"")
        for p in punctuation_space:
            line=line.replace(p," ")
        words=line.split()
        for word in words:
            if len(word)==3 and word[0] in "bB":
                print(word)

print(find_3_letter_words("input.txt"))