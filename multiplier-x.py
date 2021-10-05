
def printTafel(tafelVan: int):
    for i in range(1, 11):
        print(f'{i} x {tafelVan} = {i * tafelVan}')


tafelVan = int(input("Welke tafel wilt u?\n"))
printTafel(tafelVan)
