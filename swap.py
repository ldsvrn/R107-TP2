#!/usr/bin/env python3

a = input("Entrez la premiere  valeur : ")
b = input("Entrez la deuxieme  valeur : ")
c = input("Entrez la troisieme valeur : ")

print("Les valeurs entrees sont : a = " + a + ", b = " + b + " et c = " + c)
print("Permutation: a ==> b, b ==> c, c ==> a")
"""      *******************************************
         * Completez le programme a partir d'ici.
         *******************************************
"""

swap = a
swap2 = b
a = c
c = b
b = swap
c = swap2

"""     *******************************************
         * Ne rien modifier apres cette ligne.
         *******************************************
"""

print("Les valeurs permutees sont : a = " + a + ", b = " + b + " et c = " + c)
