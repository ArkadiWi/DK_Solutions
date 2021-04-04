# Oblicza liczby pierwsze z przedziału wprowadzonego przez użytkownika
list_of_primes = []

print('Szukanie liczb pierwszych w podanym zakresie')
try:
    min_value = int(input('Podaj wartość minimalną: '))
    max_value = int(input('Podaj wartość maksymalną: ')) + 1
except ValueError:
    print('....Podana wartość jest błędna....')
    exit()

if min_value < 2:
    print('Najmniejszą, pierwszą liczbą jest: 2, nie ma sensu podawać niższej wartości.')
    min_value = 2

for value in range(min_value, max_value):
    max_range = int(value ** 0.5) + 1
    prime = True

    for x in range(2, max_range):
        if value % x == 0:
            prime = False
            break
    if prime:
        list_of_primes.append(value)

print(list_of_primes)
