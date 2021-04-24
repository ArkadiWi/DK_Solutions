# Funkcja - wyświetla ciąg Fibonacciego do zadanego wyrażenia
def fibbonaci_seq(max: int):
    a = 0
    b = 1
    fib_list =[a]
    for i in range(max - 1):
        fib_list.append(b)
        a, b = b, a + b

    return fib_list

print(fibbonaci_seq(5))
print(fibbonaci_seq(8))
print(fibbonaci_seq(3))
print(fibbonaci_seq(1))