#recibe como parametro la operacion que debe devolver 
#no es funcional de forma rigurosa (devuelve el resultado)
def calculadora (operacion, op1, op2):
    if operacion == "+":
        return (lambda a, b: a + b ) (op1, op2)
    elif operacion == "-":
        return (lambda a, b: a - b ) (op1, op2)
    elif operacion == "*":
        return (lambda a, b: a * b ) (op1, op2)
    elif operacion == "/":
        if op2 != 0:
            return (lambda a, b: a / b ) (op1, op2)

