# Funkcja która przefiltruje słowa dłuższe niż 4 i krótsze niż 8 znaków
def proper_words(list_1: list):
   return [word for word in list_1 if 2<len(word)<8]

print(proper_words(['ala','ma','kota','i','ogromnego','psa']))