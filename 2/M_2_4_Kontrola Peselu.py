# Sprawdzenie czy nr PESEL jest zgodny
MULTIPLIER = (1,3,7,9,1,3,7,9,1,3,1)
suma = 0

try:
    pesel = int(input('Podaj swój nr pesel, musi być 11 cyfr : '))
except ValueError:
    print('Podałeś złe dane')
    exit()

pesel_2 = str(pesel)
if len (pesel_2) != 11:
    print('Podałeś złą ilość cyfr')
    exit()

for i in range(len(pesel_2)):
    suma += int(pesel_2[i]) * MULTIPLIER[i]

check_number = str(suma)
if str(check_number[-1]) == '0':
    print('Numer Pesel jest poprawny')
else:
    print('Twój nr Pesel się nie zgadza')
