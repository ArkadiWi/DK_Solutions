# Pytanie użytkownika o liczbę tak długo aż nie wpisze słow koniec następnie zwraca iloczyn wszystkich liczb
value = input('Podaj liczbe lub koniec: ')
summary = 1
while value != 'koniec':
    number = int(value)

    if number % 2 == 0:
        summary *= number
    value = input('Podaj liczbe lub koniec: ')
print(f'Iloczyn wartości parzystych wynosi: {summary}')

# 2-gie rozwiązanie Kacpra:
summary = 1
done = False
while not done:
    value = input('Podaj liczbe lub koniec: ')
    if value == 'koniec':
        done = True
        continue
    number = int(value)

    if number % 2 == 0:
        summary *= number

print(f'Iloczyn wartości parzystych wynosi: {summary}')