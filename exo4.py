#!/usr/bin/env python3

BASE = 4
ingredient= {
    "fromage": 800.0,
    "eau": 2,
    "ail": 2,
    "pain": 200
}

nbConvives = int(input("Nombres de convives: "))

for i in ingredient:
    ingredient[i] = (ingredient[i] * nbConvives) / BASE

print(ingredient)

print(f"Il vous faut:\n\t- {ingredient['fromage']}g de fromage.\n\t- {ingredient['eau']}dl d'eau.")
print(f"\t- {ingredient['ail']} gousse(s) d'ail.\n\t- {ingredient['pain']}g de pain.")