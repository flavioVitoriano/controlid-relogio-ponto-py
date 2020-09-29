#!/usr/bin/python3
from controlidpy.entities import Session
from controlidpy.functions import get_afds, get_users_from_afds, transform_afds, to_csv


session = Session("admin", "admin", "https://192.168.0.98")

day = int(input("digite o dia: "))
month = int(input("digite o mes: "))
year = int(input("digite o ano: "))

afds = get_afds(session, day, month, year)
users = get_users_from_afds(session, afds)
final = transform_afds(afds, users)

print(f"importados {len(final)} afds!")
name = input("digite o nome do arquivo para salvar: ")

to_csv(final, f"{name}.csv")
