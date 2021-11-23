#!/usr/bin/env python3

x = input("Entrez x: ")
y = input("Entrez y: ")

print(f"Avant permutation:\nx = {x}\ny = {y}\n")
temp = x
x = y
y = temp
print(f"Après permutation:\nx = {x}\ny = {y}\n")
