from abc import ABC, abstractmethod

class Notificacion(ABC):
    def __init__(self, mensaje: str, destinatario: str):
        self.mensaje = mensaje
        self.destinatario = destinatario

    @abstractmethod
    def enviar(self):
        pass

class NotificacionEmail(Notificacion):
    def enviar(self):
        print("----- EMAIL -----")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("-----------------\n")

class NotificacionSMS(Notificacion):
    def enviar(self):
        print("------ SMS ------")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("-----------------\n")

# Ejemplo de uso:
if __name__ == "__main__":
    email = NotificacionEmail("Hola, ¿cuando me traes mis croquetas?.", "ungatoconinternet@email.com")
    sms = NotificacionSMS("Hola, que no se te olviden mis croquetas.", "+123456789")
    email.enviar()
    sms.enviar()