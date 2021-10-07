def print_info(naam, leeftijd):
    print(f'Hallo {naam}, je leeftijd is {leeftijd} jaar')


while True:
    naam = input('Wat is uw naam? Of wil je stoppen?')

    if naam == 'stop':
        break

    leeftijd = input('Wat is uw leeftijd?')

    print_info(naam, leeftijd)
