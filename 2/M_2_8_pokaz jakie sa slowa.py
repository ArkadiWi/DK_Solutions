# Odbierz słowa oddzielone przecinkami i wyświetl każde w nowej linii
words = set(input('Podaj słowa oddzielone przecinkami: ').replace(',', '').split())
print(words)
for word in words:
    print(word)
