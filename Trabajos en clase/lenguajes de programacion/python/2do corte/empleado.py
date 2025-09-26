from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str, id_empleado: int):
        self.nombre = nombre
        self.id_empleado = id_empleado

    @abstractmethod
    def calcular_pago(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, id_empleado: int, salario_mensual: float):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual

class EmpleadoTiempoMedido(Empleado):
    def __init__(self, nombre: str, id_empleado: int, horas_trabajadas: float, pago_por_hora: float):
        super().__init__(nombre, id_empleado)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self):
        return self.horas_trabajadas * self.pago_por_hora

class EmpleadoPrestacionServicios(Empleado):
    def __init__(self, nombre: str, id_empleado: int, monto_contrato: float):
        super().__init__(nombre, id_empleado)
        self.monto_contrato = monto_contrato

    def calcular_pago(self):
        return self.monto_contrato

if __name__ == "__main__":
    emp1 = EmpleadoTiempoCompleto("Ana", 1, 35000)
    emp2 = EmpleadoTiempoMedido("Luis", 2, 76, 55)
    emp3 = EmpleadoPrestacionServicios("Carlos", 3, 8000)

    print(f"{emp1.nombre} cobra: ${emp1.calcular_pago()}")
    print(f"{emp2.nombre} cobra: ${emp2.calcular_pago()}")
    print(f"{emp3.nombre} cobra: ${emp3.calcular_pago()}")