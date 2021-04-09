# Funkcja ktora zwraca najwiekszy wspolny dzielnik
def finding_highest_common_divider(a: int, b: int):
    a_div = set(x for x in range(1,a+1) if a % x == 0)
    b_div = set(x for x in range(1,b+1) if b % x == 0)
    return max(a_div & b_div)

print(finding_highest_common_divider(50,73))