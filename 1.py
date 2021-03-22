value = int(input('Podaj liczbe:.. '))

if value % 55 == 0:
    print('Jest podzielna przez 5 i 11')
elif value % 5 == 0:
    print('Jest podzielna przez 5')
elif value % 11 == 0:
    print('Jest podzielna przez 11')
else:
    print('Nie jest podzielna przez 5 i 11')

print('\n\tPodaj współrzędne wierzchołków trójkąta')
top_a1 = int(input('Wierzchołek A1: '))
top_a2 = int(input('Wierzchołek A2: '))
top_b1 = int(input('Wierzchołek B1: '))
top_b2 = int(input('Wierzchołek B2: '))
top_c1 = int(input('Wierzchołek C1: '))
top_c2 = int(input('Wierzchołek C2: '))
