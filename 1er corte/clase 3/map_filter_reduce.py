from functools import reduce

# MAP / FILTER / REDUCE


# A) : "mapea" una funcion a todos los elementos de una lista

#ejemplo: conversion de divisas (1 USD =  4100 COP): 
precios_dolares =[45, 35, 25, 18, 24, 26, 47, 19]

precios_pesos = list(map(lambda x: x * 4100.0, precios_dolares))

print(f"precios en dolares: {precios_dolares}")
print(f"precios en pesos: {list(precios_pesos)}")

# B) FILTER: filtra los elementos de una lista que cumplen una condicion
# vamos a filtrar los precios menores a 100000.0 

lista_filtrada = list(filter(lambda x: x <= 100000.0, precios_pesos))
print(f"lista filtrada: {lista_filtrada}")


# C) REDUCE: reduce los elementos de una lista a un solo valor, aplicando una funcion que recibe dos parametros
suma_precios = reduce(lambda x,y: x+y, lista_filtrada)
print(f"suma de precios: {suma_precios}")

# EJERCICIO:
lista = ["muchos", "años", "despues","frente","al","peloton","de", "fusilamiento","el","coronel","Aureliano","Buendia","habia","de","recordar","aquella","tarde","remota","en","que","su","padre","lo","llevó","a","conocer","el","hielo"] 

#1. convertir a mayusculas
#2. armar un solo tetxo
lista_mayusculas = list(map(lambda x: x.upper(), lista))
print(f"lista en mayusculas: {lista_mayusculas}")
texto = reduce(lambda x,y: x + " " + y, lista_mayusculas)
print(f"texto: {texto}")
