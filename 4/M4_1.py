# M4_ 1 funkcja odbierająca arg w postaci listy
def group_them(*args, **kwargs):
    for keys, values in kwargs.items():
        print(f'{keys.capitalize()} is {values}')


group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green')
