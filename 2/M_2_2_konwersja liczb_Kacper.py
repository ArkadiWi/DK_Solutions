# Konwersj aliczb - rozwiązanie Kacpra
option = input('Co chceszx zamienić \t(1) dwójkowa \t(2) dziesiętna ')
if option == '1':
    value = input('Podaj wartośc w systemie dwójkowym: ')
    result = 0
    for index, number in enumerate(value):
        result += int(number) * 2 ** ((len(value)) - index - 1)
        print(f'{index}: Wartość = {result}')
    print(f'Wartość w systemie binarnym to: {result}')

elif option == '2':
    pass
else:
    print('Wybrałeś złą opcję.')