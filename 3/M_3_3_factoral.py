#Funkcja która liczy silnie dla podanej liczby
def get_factorial (number: int = 1 ):
    a = 1
    while number > 0:
        a *= number
        number -= 1
    return a

try:
    num = int(input('Podaj do ilu chceszliczyć silnię: '))
except ValueError:
    print('Popdałeś niewłaściwą liczbę')

print(f'Silnia dla {num} wynosi: {get_factorial(num)}')
