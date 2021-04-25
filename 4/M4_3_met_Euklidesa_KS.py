# Znajdż zajwiększy wspólny dzielnik metodą Euklidesa:

def euklides_gd(a: int, b: int) -> int:
    if b == 0:
        return a
    print(f'a = {a}, b = {b}')
    return euklides_gd(b, a % b)


def euklides_while(a:int, b:int) -> int:
    while b != 0:
        c = a % b
        print(f'1: a = {a}, b = {b}, c = {c}')
        a, b = b, c
        print(f'2: a = {a}, b = {b}, c = {c}')
    return a

# euklides_while(10,30)
print(euklides_gd(4,11))

def test_euklides_while():
    assert euklides_while(30, 10) == 10

def test_euklides_gd():
    assert euklides_gd(10, 30) == 10