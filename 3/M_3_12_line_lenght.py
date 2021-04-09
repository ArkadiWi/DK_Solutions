# Funkcja - liczy długośc odcinka z 2 współrzędnych
from typing import Tuple
from math import sqrt


def line_lenght(a: Tuple[int, int], b: Tuple[int, int]):
    return sqrt((b[0] - a[0]) ** 2 + (b[1] - a[0]) ** 2)


print(line_lenght((1, 1), (2, 2)))
print(line_lenght((5, 6), (10, 20)))
