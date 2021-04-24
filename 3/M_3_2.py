# Pytanie użytkownika o liczbę tak długo aż nie wpisze słow koniec następnie zwraca iloczyn wszystkich liczb
numbers = []
while True:
    number = input('Podaj liczbę, lub wpisz "zakończ", lub "z" aby zakończyć: ')
    if number in ('zakończ', 'zakoncz', 'z'):
        break
    try:
        int(number)
        numbers.append(int(number))
    except ValueError:
        continue

c = 1
score = [x for x in numbers if x % 2 == 0]2

for i in range(len(score)):
    c *= score[i]
print(f'Suma liczb parzystych wynosi: {c}')


