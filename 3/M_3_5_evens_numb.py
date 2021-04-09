# Filtruje liczby parzyste z listy w argumencie
def get_even_numbers(list_1:list):
    even_numbers = [number for number in list_1 if number % 2 == 0 ]
    return even_numbers

print(get_even_numbers([1,2,3,4,5,6,8]))