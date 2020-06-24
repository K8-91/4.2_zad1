def palindrom_check(word):
    word_normal=[]
    word_backward=[]
    for letter in word:
        word_normal.append(letter)
        word_backward.insert(-len(word),letter)
    palindrom_result= bool(word_normal==word_backward)
    return palindrom_result