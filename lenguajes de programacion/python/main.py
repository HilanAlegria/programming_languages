from calculadora import *

def division(a,b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    operacion = input("Ingrese la operación (+, -, *, /): ")
    funcion = None
    operacion1 = int (input("Ingrese el primer operandor: "))
    operacion2 = int (input("Ingrese el segundo operandor: "))
    resultado = calculadora(operacion,(operacion1),(operacion2))
    print(f"!el resultado es: {resultado}") #¿?+

    #version 1, funcion lambda
    #version 1: asiganmos la funcion a la variables de acuerdo  al operador, con una funcion lambda

    if operacion == "+":
        funcion == (lambda a, b: a + b) #funcion sin nombre, que recibe dos argumentos, y los suma
    elif operacion == "-":
        funcion == (lambda a, b: a - b) #funcion sin nombre, que recibe dos argumentos, y los resta
    elif operacion == "*":
        funcion = (lambda a, b: a * b)
    elif operacion == "/":
        funcion = division

    resultado = funcion(operacion1, operacion2)

    resultado2 = calculadora(operacion) (operacion1, operacion2)


    operaciones ={
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }

    resultado3 = operaciones[operacion](operacion1, operacion2)


    print(f"¡El resultado es: {resultado}")
    print(f"otra version del resultado es: {resultado2}")
    print(f"otra version del resultado es: {resultado3}")