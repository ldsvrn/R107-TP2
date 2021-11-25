while True:
    nb = int(input("Entrez un nombre: "))
    if nb != 0: print(f"Votre nombre est {'négatif' if nb < 0 else 'positif'} et {'pair' if nb % 2 == 0 else 'impair'}")
    if nb == 0: print("Le nombre est zéro (et il est pair)")
