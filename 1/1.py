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
ax = float(input('Wierzchołek ax: '))
ay = float(input('Wierzchołek ay: '))
bx = float(input('Wierzchołek bx: '))
by = float(input('Wierzchołek by: '))
cx = float(input('Wierzchołek cx: '))
cy = float(input('Wierzchołek cy: '))


sec_AB = ((bx-ax)**2 + (by-ay)**2)**0.5
sec_BC = ((cx-bx)**2 + (cy-by)**2)**0.5
sec_AC = ((cx-ax)**2 + (cy-ay)**2)**0.5
circuit = sec_AB + sec_BC + sec_AC
print(f'Obwód trójkąta wynosi: {circuit}')
area_of_triangle = 0.5*((bx-ax)*(cy-ay)-(by-ay)*(cx-ax))
print(f'Pole trókąta wynosi: {abs(area_of_triangle)}')
