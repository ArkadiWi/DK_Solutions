# Szyfr Cezara
abc = ''
cba = ''

word = input('Podaj słowo do zaszyfrowania: ')
try:
    cipher = int(input('Podaj wielkość klucza: '))
except ValueError:
    print('Podałeś złą wartość klucza!!!!')

# Szyfrowanie wiadomości:
for char in word:
    abc += chr(ord(char) + cipher)

print(f'Zakodowana wiadomość: {abc}')

# Deszyfrowanie wiadomości:
print('\n\tA teraz odszyfrujemy tę wiadomość \n')
for char in abc:
    cba += chr(ord(char) - cipher)
print(f'Odkodowana wiadomość: {cba}')
