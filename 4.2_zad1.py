def palindrom_check(word):
    word_normal=[]
    word_backward=[]
    for letter in word:
        word_normal.append(letter)
        word_backward.insert(-len(word),letter)
    palindrom_result= bool(word_normal==word_backward)
    return palindrom_result


print(palindrom_check('kot'))
print(palindrom_check('kajak'))

def palindrom_sprawdzenie(slowo):
    slowo_normal=[]
    for litera in slowo:
        slowo_normal.append(litera)
    palindrom_result2=bool(slowo_normal==slowo_normal[::-1])
    return palindrom_result2


print(palindrom_sprawdzenie('kajak'))
