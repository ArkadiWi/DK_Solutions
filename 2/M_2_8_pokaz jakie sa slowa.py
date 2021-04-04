# Odbierz słowa oddzielone przecinkami i wyświetl każde w nowej linii
words = list(input('Podaj słowa oddzielone przecinkami: ').replace(',', ' ').split())
for word in words:
    print(word)
