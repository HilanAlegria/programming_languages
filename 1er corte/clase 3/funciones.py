
#3. funciones puras e inmutabilidad:
# en programacion funcional, la inmutabilidad significa que los datos no cambian despues de ser creados
# en lugar de modificar estrucutras de datos (listas, diccionarios, etc.), se generan nuevas estructuras con los cambios deseados)
# esto evita efectos secundarios y hacer que ele comportamiento del programa sea mas predecible
    
lista_nombres =["Diego","Diana","Maria","Pedro","Juan"]
lista_nombres = lista_nombres + ["Camila"]
lista_nombres_nueva = lista_nombres + ["Mariana"]
    
print(lista_nombres)
print(lista_nombres_nueva)   
    
    
    #Funciones puras:
    # una funcion puyra es aquella que:
    # a) seimpre devuelve el mismo resultado para los mismos argumentos
    # b) no tiene efectos secundarios (no modifica ningun estado externo ni depende de el)
    
def cube(x):
    return x*x*x
    
print(f"el cubo de 4 es {cube(4)}")
    
def CRUD_add(lista, nuevo_elemento):
    return lista + [nuevo_elemento]
    
    #version no pura
def CRUD_add(lista, nuevo_elemento):
    lista = lista + [nuevo_elemento]
    return lista
    
    #funcion pura con diccionarios
def CRUD_update_dicc(dic, clave, valor):
    nuevo_dic = dic.copy()
    nuevo_dic [clave] = valor
    return nuevo_dic
        
    
print(f"nueva lista {CRUD_add(lista_nombres, 'Valentina')}")
    
    
dic_bd = {"nombre": "Diego",
        "estatura": 1.60,
        "edad": 23,
        "peso": 62.0,
        }
    
print(f"datos sin actualizar: {dic_bd }")
    
print(f"datos actualizados: {CRUD_update_dicc(dic_bd, 'edad', 24)}")
    
print(f"datos originales: {dic_bd }")
    
    
#funciones de orden superior:
# 1. son funciones que reciben oras funciones como argumentos o devuelven funciones como resultado

# a) funcion que recibe otra funcion como parametro:

def aplicar_operacion(func, x, y):
    return func(x, y)

print(f"aplicando una suma: {aplicar_operacion(lambda a,b: a+b, 89,63)}")
print(f"aplicando una resta: {aplicar_operacion(lambda x,y: x-y, 42, 19)}")

# b) una funcion que devuelve otra funcion:
def multiplicacior(n):
    def f(x):
        return n * x
    return f
duplicar = multiplicacior(2) #duplicar es una funcion
triplicar = multiplicacior(3) # triplicar es una funcion

print(f"duplicando 88: {duplicar(88)}")
print(f"triplicando 77: {triplicar(77)}")

# map / filter / reduce:




    