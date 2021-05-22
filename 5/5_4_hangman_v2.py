import random


def wprowadz_litere():
    letter = input('\nWprowadź literę: ')

    if letter not in FORBIDDEN_SIGNS and len(letter) == 1:
        global guess
        guess = letter.upper()
        return guess
    else:
        if len(letter) > 1:
            print('Wprowadż tylko 1 znak')
        else:
            print('Wprowadź literę a nie cyfrę lub inny durny znak')
        wprowadz_litere()


FORBIDDEN_SIGNS = ' 01234567890?~`!@#$%^&*()_+-/\\<>,.;:"}{[]|\''
SOURCE = ['W-', 'I-', 'S-', 'I-', 'E-', 'L-', 'E-', 'C']
FINAL_JUDGMENT = 'W-I-S-I-E-L-E-C'

words = []
with open('5_4_words.txt', 'r', encoding='utf8') as handler:
    lines = handler.readlines()
    for line in lines:
        words.append(line.upper().strip())


word = random.choice(words)  # słowo do odgadnięcia
so_far = '-' * len(word)  # kreska zastępuje nieodgadniętą literę
wrong = 0  # liczba nietrafionych liter
used = []  # litery już użyte w zgadywaniu
judgment = ''

print('Witaj w grze szubienica. Good luck!!')

while judgment != FINAL_JUDGMENT and so_far != word:  # główna pętla programu
    print(f'Wykorzystałeś już następujące litery: {used}')
    print(f'Na razie zagadkowe słowo wygląda tak: {so_far}')
    print(f'Twój stan: {judgment}')
    guess = ''
    wprowadz_litere()

    while guess in used:  # sprawdzenie, czy już nie podano tej litery wcześniej
        print('Już wykorzystałeś literę: ', guess)
        wprowadz_litere()

    used.append(guess)

    if guess in word:  # sprawdzenie, czy litera jest w słowie
        print('Tak! ', guess, 'znajduje się w szukanym słowie!')

        new = ''  # utworzenie nowej zmiennej i dodanie do niej litery
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new         # KONKATENACJA: np.: ('-' + '-' + 'A' + '-' + 'A')
    else:
        print('\nNiestety ', guess, 'nie występuje w szukanym słowie')
        judgment += SOURCE[wrong]
        wrong += 1

if judgment == FINAL_JUDGMENT:
    print(judgment)
    print('Zostałeś powieszony')
else:
    print('Odgadłeś!')

print('Zagadkowe słowo to: ', word)
input('Aby zakonczyć program, naciśnij cokolwiek.')