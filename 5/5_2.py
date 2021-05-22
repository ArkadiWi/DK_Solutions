from datetime import date

def input_product():
    set_of_prod = set()

    while True:
        product = input('Podaj nazwę produktu: ').lower()
        if product != 'koniec':
            set_of_prod.add(product)
        else:
            return set_of_prod

current_data = date.today().strftime("%d_%m_%Y")

with open(f'{current_data}.txt', 'w', encoding = 'utf8') as handler:
    products = input_product()
    for product in products:
        handler.write(f'{product}\n')



