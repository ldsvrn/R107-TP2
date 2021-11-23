#!/usr/bin/env python3

import datetime
time = datetime.datetime.now().date()

age = int(input("Votre âge: "))
print(f"Vous êtes né en {int(time.year)- age}")
