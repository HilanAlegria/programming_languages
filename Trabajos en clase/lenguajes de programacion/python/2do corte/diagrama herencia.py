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


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre: str, id_empleado: int, horas: int, tarifa: float):
        super().__init__(nombre, id_empleado)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa

class Notificacion(ABC):
    def __init__(self, mensaje: str, destinatario: str):
        self.mensaje = mensaje
        self.destinatario = destinatario

    @abstractmethod
    def enviar(self):
        pass


class NotificacionEmail(Notificacion):
    def enviar(self):
        print("📧 EMAIL")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("------------------\n")


class NotificacionSMS(Notificacion):
    def enviar(self):
        print("📱 SMS")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("------------------\n")


if __name__ == "__main__":

    emp1 = EmpleadoTiempoCompleto("Ana", 1, 3000)
    emp2 = EmpleadoPorHoras("Luis", 2, 120, 25)

    pago1 = emp1.calcular_pago()
    pago2 = emp2.calcular_pago()

    noti1 = NotificacionEmail(f"Hola {emp1.nombre}, tu pago es ${pago1}.", "ana@email.com")
    noti2 = NotificacionSMS(f"Hola {emp2.nombre}, tu pago es ${pago2}.", "+123456789")

    noti1.enviar()
    noti2.enviar()
