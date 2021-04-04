# Sprawdzanie czy palindrom i czy anagram
while True:
    choice = input('\t[1] Palindrom \t[2] Anagram \t[3] koniec programu\n')

    # Palindrom:
    if choice == '1':
        check_word = input('Podaj słowo do sprawdzenia czy palindrom: ').replace(' ', '').lower()

        if check_word == check_word[::-1]:
            print(f'Podane hasło {check_word} jest palindromem')
        else:
            print(f'Podane hasło {check_word} nie jest palindromem.')

    # Anagram
    elif choice == '2':
        angram_score = True
        anagr_1 = list(input("Podaj słowo do Anagramu: ").replace(' ', '').lower())
        anagr_2 = list(input("Podaj słowo kontrolne do Anagramu: ").replace(' ', '').lower())

        if len(anagr_1) > len(anagr_2):
            angram_score = False

        if angram_score:
            for char in anagr_1:
                try:
                    indx = anagr_2.index(char)
                    del anagr_2[indx]
                except ValueError:
                    angram_score = False
                    break

        if angram_score:
            print('To jest anagram')
        else:
            print('To hasło nie jest anagramem')

    elif choice == '3':
        exit()

    else:
        print('Błędny wybór, spróbuj ponownie')