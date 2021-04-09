# Funkcja - liczy znaki w nawiasach:
def count_letters(text: str, start='(', end=')'):
    copy = False
    char_list = []
    for char in text:
        if char == start:
            copy = True
            continue
        if char == end:
            copy = False
        if copy:
            char_list.append(char)
    return len(char_list)


print(count_letters('(ala) ma (kota)'))
print(count_letters('<> kod <103>', '<', '>'))
print(count_letters('abrakadabra'))
