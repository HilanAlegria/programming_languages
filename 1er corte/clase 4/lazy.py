from functools import reduce

# ejemplo 1 eager evaluation: evalucion inmediata un producor de la dato de 100.000 usuarios:
# data set
# ----- prodcutor
usuarios = []
for i in range(50000000):
    if i % 3 == 0:
        usuarios.append(f"user{i}@gmail.com")
    else:
        usuarios.append(f"user{i}@hotmail.com")
        
#filtrar los usuarios de gmail
# ----- consumidor 
usuarios_gmail = []
for u in usuarios:
    if "gmail" in u:
        usuarios_gmail.append(u)
        
#impimir los usuarios de gmail
print(usuarios_gmail[:5])
        
#ejemplo 2
# lazy evaluation: evalucion perezosa un producor de la dato de 100.000 usuarios:
#producto perezoso:
def generar_user_data():
    for i in range(50000000):
        if i % 3 == 0:
            #YIELD genera el valor si lo piden y pausa el ciclo hasta que le piden el sigueinte dato
            yield f"user{i}@gmail.com"
        else:
            yield f"user{i}@hotmail.com"

# consumidor perezoso
#asignamos la funcion del productor perezoso a un generador:
fuente_datos = generar_user_data()

#el consumidor pide datos de forma perezosa:
#pide 4 datos

print("genarador y consumidor perezosos (lazy):")
dato = next(fuente_datos)
print(dato)
nuevo_dato = next(fuente_datos)
print(nuevo_dato)
otro_dato = next(fuente_datos)
print(otro_dato)
y_otro_dato = next(fuente_datos)
print(y_otro_dato)

#como lo hacemos dade un ciclo?:
#pedimos primero 100

#EJECERCICIO 1:

dara_gmail = []
data_hotmail = []

for i in range(100):
    try:
        data = next(fuente_datos)
        #filtrar y agregar a la lista de hotmal o la de gmail
    except StopIteration:
        print("el generador no puede genarar mas datos")
        
#hacerlo con otros 100 datos
for i in range(100):
    try:
        data = next(fuente_datos)
        #filtrar y agregar a la lista de hotmal o la de gmail
    except StopIteration:
        print("el generador no puede genarar mas datos")

            
#EJERCICIO 2: (lazy evaluation, map, filter, reduce)
# genere de forma perezosa los numeros naturales hasta 50000000.
#filtre solo aquellos que sean multiplos de 5.
#tranforma solo los primeros 10 resultados
#calcule la suma ototal de esos 10 numeros procesados usando reduce

def generar_numeros():
    
    nums = []
    for i in range(100):
        nuevo_num = next(generar_numeros)
        nums.append(nuevo_num)
















#ejemplo 3