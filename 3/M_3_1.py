#wynik funkcji - lista z sumami 2 podanych list
def sum_lists (lista_1:list, lista_2: list) -> float:
    summary = [a + b for a, b in zip(lista_1, lista_2)]
    return summary

a = [2,4,6]
b = [8,6,4]
print(sum_lists(a,b))
