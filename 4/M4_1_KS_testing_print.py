# M4_ 1 funkcja odbierająca arg w postaci listy_ rozw Kacpra
def group_them( **kwargs):
    for key, value in kwargs.items():
        print(f'{key.capitalize()} is {value}')


group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green')

# testowanie wyświetlania
def test_group_them(capsys):
    group_them(wall='red', tomato='red', light='yellow')
    out, err = capsys.readouterr() # ta linia zczytuje to, co się już wyświetliło, dlatego jest po linijce wywołującej funkcję
    assert out == 'Wall is red\nTomato is red\nLight is yellow\n' # znak \n zawsze jestna koniec linii print()