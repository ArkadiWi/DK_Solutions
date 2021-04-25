# sumuj wyrażenia z ciągu Fubonacciego - rekurencja, rozwiązanie Kacpra

def fibonacci_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
# ta jedynka na końcu "nabija" licznik dla 5 rekurencja odbywa się 7 razy i stąd  taki wynik :-)
    return fibonacci_sum(n - 1) + fibonacci_sum(n - 2) + 1
print(fibonacci_sum(5))


def test_fiboonacci_sum():
    assert fibonacci_sum(0) == 0
    assert fibonacci_sum(1) == 0
    assert fibonacci_sum(2) == 1
    assert fibonacci_sum(3) == 2
    assert fibonacci_sum(5) == 0+1+1+2+3

