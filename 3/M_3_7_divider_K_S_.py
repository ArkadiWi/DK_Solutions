# Funkcja ktora zwraca najwiekszy wspolny dzielnik
def find_divisors(a):
    return {d for d in range(2, a + 1) if a % d == 0}


def find_greatest_divisor(a, b):
    div_a = find_divisors(a)
    div_b = find_divisors(b)
    return max(div_a & div_b)

print(find_greatest_divisor(1568, 100064))