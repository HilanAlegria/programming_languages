from abc import ABC, abstractmethod

# conceptos basicos de OOP en python
# Abstracción, Encapsulamiento, Herencia, Polimorfismo

# atributos de clase (estaticos) vs.  atributos de instancia 
# de obejto (requieren creación)
class Estudiante:
    
    # atributo de clase (estatico)
    universidad = "Universidad Santiago de Cali"
    
    # metodo de instancia (crean objetos)
    # recibe como primer parametro, refenrencia a la instancia
    def __init__(self, nombre: str, ciudad: str, carrera: str):
        self.nombre = nombre
        self.ciudad = ciudad
        self.carrera = carrera
        self.cursos = []
    # metodo de instancia
    def matricular_curso(self, curso: str ):
        self.cursos.append(curso)
    
    @classmethod
    def cambiar_razonsocial(cls, nuevaRazonSocial):
        cls.universidad = nuevaRazonSocial
    
e1 = Estudiante("Hilan", "Cali", "Ingenieria de Sistemas")
e2 = Estudiante("Ana", "Palmira", "Medicina")

print(f"El Estudiante {e1.nombre} de la {e1.cambiar_razonsocial} es de {e1.ciudad}")
e1.cambiar_razonsocial("quiero destruccion quiero estudiar en la Universidad del Valle")
print(f"El Estudiante {e2.nombre} de la {e2.cambiar_razonsocial} es de {e2.ciudad}")
print(f"El estudiante {e1.nombre} de la {e1.cambiar_razonsocial} es de {e1.ciudad}")

# abstraccion + encapsulamiento
# clase abstracta

class Cuenta(ABC):
    
    # metodo de instancia
    def __init__(this, titular:str, numcuenta:str, saldo:float):
        this.__titular = titular
        this.__numcuenta = numcuenta
        this.__saldo = saldo
        
    # los metodos abstractos no tienen implementacion, 
    # la implementacion la hacen las clases hijas
    @abstractmethod
    def calcular_rendimiento(this):
        pass
    
    # los metodos no abstractos o concretos pueden ser heredados de las subclases:
    # (¿se puede sobreescribir?)
    def consultar_saldo(this):
        return f"El saldo de la cuenta es: {this.__saldo}"
    
    def depositar(this, monto:float):
        this.saldo = this.saldo - monto
        
    def retirar (this, monto:float):
        this.saldo = this.saldo - monto
        
class CuentaAhorros(Cuenta):
    
    porc_rend = 0.1
    
    def calcular_rendimiento(this):
        # Ejecicion: implementar de acuerdo al atributo de clase propio de cuenta corriente
        return super().calcular_rendimiento()

class CuentaCorriente(Cuenta):
    
    porc_rend = 0.2
    
    def consultar_saldo(this):
        # se sobreescribe:
        return super().consultar_saldo()
    def calcular_rendimiento(this):
        # Ejecicion: implementar de acuerdo al atributo de clase propio de cuenta corriente
        return super().calcular_rendimiento()
    
cuenta1 = CuentaAhorros("Hilan", 248032, 180000000)
cuenta2 = CuentaCorriente("Ana", 67890, 200000000)

print(cuenta1.consultar_saldo())
print(cuenta2.consultar_saldo())