# Funkcja - wyświetla ciąg Fibonacciego do zadanego wyrażenia
def fibbonaci_seq(max: int):
    fib_list = []
    a = 0
    b = 1
    fib_list.append(a)
    for i in range(max - 1):
        fib_list.append(b)
        a, b = b, a + b

    return fib_list

print(fibbonaci_seq(10))
