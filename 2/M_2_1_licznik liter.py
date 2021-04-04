# How many signs in word
dict_word = {}
word = tuple(input('Podaj słowo: '))

for char in word:
    if char not in dict_word:
        dict_word[char] = 0
    dict_word[char] += 1

for char, value in dict_word.items():
    print(f'\tW tym słowie litera {char} występuje {value} raz(y)')