#!/bin/python3
try:
	a = int(input("ingresa un numero: "))
	print(f"impresion: {a}")
except ValueError:
	print("Debe ser solo numeros")
