word=input('enter word: ')
reversed_word=''
for x in word:
    reversed_word=reversed_word+x
if word==reversed_word:
    print(f'word {word} is palindrom')