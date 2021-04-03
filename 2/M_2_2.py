# Zamiana wartości dziesiętnych i binarnych:
binar = True
choice = input('Z dzisiętnej na binarną [1] Z binarnej na dziesiętną [2] ')
if choice == '1':
    pass
elif choice == '2':
    binar = False
else:
    print('Błędny wybór')

if binar:
    try:
        value = int(input('Podaj wartość dziesiętną: '))
        # sposób nr 1
        binar = bin(value).replace('0b', '')
        print(f'Wartość dziesiętna: {value} , wartość binarna to: {binar}')
        # sposób nr 2
        wynik = []
        value_2 = value
        while value_2 != 0:
            wynik.insert(0, value_2 % 2)
            value_2 = value_2 // 2
        print(f'Liczba {value} to w zapisie dwójkowym:', end='')
        for i in wynik:
            print(i, end='')

    except ValueError:
        print('\t\tŹle wpisana wartość')

else:
    try:
        binar = input('Podaj wartość binarną: ')
        # sposób nr 1
        print(f'(1) Wartośc binarna: {binar}, wartość dziesiętna to: {int(binar, 2)}')
        # sposób nr 2
        x = 0
        suma = 0
        for char in binar[::-1]:
            if char == '1':
                suma += 2 ** x
            x += 1
        print(f'(2) Wartość dziesiętna z liczby {binar} to: {suma}')
        # sposób nr 3
        x = 0
        suma = 0
        for char in binar[::-1]:
            if char == '1':
                suma += 1 << x
            x += 1
        print(f'(3) Wartość dziesiętna z liczby {binar} to: {suma}')
    except ValueError:
        print('\t\tŹle wpisana wartość')
