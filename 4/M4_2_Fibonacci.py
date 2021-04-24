# sumuj wyrażenia z ciągu Fubonacciego - rekurencja
from math import sqrt


def fibonacci_sum(n):
    if n == 0:
        return 0
    list_number = [0]
    while n > 0:
        list_number.insert(1,int(round(((1 / sqrt(5)) * (((1 + sqrt(5)) / 2) ** n)), 0)))
        n -= 1
        fibonacci_sum(n)
    list_number.pop()
    return (list_number)


print(sum(fibonacci_sum(10)))
