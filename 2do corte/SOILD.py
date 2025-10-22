# SOILD principles in Python
# 1. Single Responsibility Principle (SRP): una clase tiene una unica responsabilidad en el modulo que hace parte

# no aplicado:

class Report:
    
    def __init__(this, data):
        this.data = data
    
    def calcular_estads(this):
        pass
    
    def generarArchivo(this, tipoArchivo):
        if tipoArchivo == 'EXCEL':
            print("Generando reporte en EXCEL")
        elif tipoArchivo == 'PDF':
            print("Generando reporte en PDF")
        else:
            print("Tipo de archivo no soportado")
    
    def notificarCambios(this):
        print("hubo cambios en los datos:{this.data}")
    
# cual es la solucion? separando en responsabilidades, se separa en 3 clases diferentes:


# 2. Open / Closed: poen for extension, closed for modification

# no aplicado:

class Sales_Discount:
    
    def __init__(this, tipo_cliente):
        this.tipo_cliente = tipo_cliente
    
    def aplicarDescuento(this, total_compra):
        if this.tipo_cliente == "regular":
            print("decuento para cliente regular")
        elif this.tipo_cliente == "VIP":
            print("descuento para cliente VIP")

# que pasa si se quiere agregar un descuento para un nuevo tipo de cliente? 

# separar en funciones de la misma clase o en clases distintas, oaplicar strategy 

# 3. Liskov sustitution principle: es un modulo de software donde se implmente generalizacion a travez de herencia,
#       deberia usarse la subclase en reemplazo de la superclase, y viceversa.

class Ave:
    
    def __init__(this):
        pass
    
    def volar():
        print("Volando")
    
class Avestruz(Ave):
    
    def vloar():
        raise Exception("Las avestruces no pueden volar")

# Solucion: generalizar más 

class Ave:
    # no implementa metodos que las aves no voladores no expongan: 
    pass

class AveVoladora(Ave):
    def __init__(this):
        pass
    
    def volar():
        print("Volando")

class Avestruz(Ave):
    def volar():
        raise Exception("Las avestruces no pueden volar")
    
