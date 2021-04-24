# Znajdż zajwiększy wspólny dzielnik metodą Euklidesa:

def euklides(a: int, b: int) -> int:
    if a > b:
        c = a - b
        euklides(c, b)

    elif a < b:
        c = b - a
        euklides(c, a)
    return a


print(euklides(10, 30))


def test_euklides():
    assert euklides(10, 30) == 10
