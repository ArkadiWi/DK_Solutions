#Zlicza samogłoski
def count_vowels (text: str):
    return sum([char in 'aeiouyąę'for char in text])


print(count_vowels('ala'))
print(count_vowels('programowanie'))