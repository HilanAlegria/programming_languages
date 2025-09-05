from itertools import islice

# Generador perezoso de números naturales 
def naturales_hasta(n):
    for i in range(n):
        yield i

# el oso perezoso
naturales = naturales_hasta(50000000)
multiplos_de_5 = filter(lambda x: x % 5 == 0, naturales)
# se convierte a lista para mostrar
primeros_10 = list(islice(multiplos_de_5, 10))  

print("Primeros 10 múltiplos de 5:", primeros_10)

# se muestra lista de los numeros
cuadrados = list(map(lambda x: x ** 2, primeros_10))
print("Cuadrados de esos múltiplos:", cuadrados)

#se muestra la suma
suma_total = sum(cuadrados)
print("La suma total es:", suma_total)