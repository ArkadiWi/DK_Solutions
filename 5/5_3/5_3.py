# znajdz pliki z rozsz .txt
# scal stringi i zapisz w scalone.txt
import pathlib

files = list(pathlib.Path('D:\\Python391\\!_Python_nauka\\DoKodu\\DK_Homeworks\\5\\5_3').glob('*.txt'))
new_string = ''
for file in files:
    with open(file, 'r', encoding='utf8') as handler:
        line = handler.read()
        new_string += line + ' '
print(new_string)


