import random
from abc import ABC, abstractmethod

# =================================================================
# 1. ABSTRACCIÓN DEL PATRÓN OBSERVER (Contrato)
# =================================================================

class Observer(ABC):
    """Define la interfaz de reaccion para el Control Maestro."""
    @abstractmethod
    def update(self, subject: 'Subject', datos_cambio: dict):
        pass

class Subject(ABC):
    """Clase base para los Subsistemas que seran observados."""
    def __init__(self):
        self._observadores = []

    def attach(self, observer: Observer):
        """Adjunta un observador."""
        if observer not in self._observadores:
            self._observadores.append(observer)

    def notificar(self, datos_cambio: dict):
        """Notifica a todos los observadores de un cambio importante."""
        print(f"[{self.__class__.__name__}] Estada crítico. Notificando...")
        for observador in self._observadores:
            observador.update(self, datos_cambio)

# =================================================================
# 2. SUBSISTEMAS (SUJETOS - Solo lo esencial)
# ==========

# Simulamos la existencia de un repositorio de luces para mantener SRP
class RepositorioLuces:
    def __init__(self):
        self._data = {'L101': 'OFF', 'ALARM': 'OFF'}
    def get_state(self, id):
        return self._data.get(id)
    def update_state(self, id, state):
        self._data[id] = state

class LightModel(Subject):
    """Gestiona luces y notifica si se activa la alarma."""
    def __init__(self, repo):
        super().__init__()
        self.repository = repo

    def toggle_light(self, light_id: str):
        current = self.repository.get_state(light_id)
        if current:
            new_state = "ON" if current == "OFF" else "OFF"
            self.repository.update_state(light_id, new_state)

            # Lógica de notificación
            if light_id == "ALARM" and new_state == "ON":
                self.notificar({"evento": "ALARMA_ACTIVADA", "detalle": "Luz de seguridad encendida."})
            return True
        return False

class TempModel(Subject):
    """Gestiona temperatura y notifica al superar el umbral."""
    def __init__(self):
        super().__init__()
        self.temp_actual = 23.0
        self.umbral = 30.0

    def medir(self):
        self.temp_actual += random.uniform(-1.0, 2.5)
        self.temp_actual = round(self.temp_actual, 1)

        # Lógica de notificación 
        if self.temp_actual >= self.umbral:
            self.notificar({"evento": "TEMP_CRITICA", "valor": self.temp_actual})
        return self.temp_actual

# =================================================================
# 3. CONTROL MAESTRO (OBSERVADOR)
# =================================================================

class ControlMaestro(Observer):
    """El controlador central que reacciona a los eventos del sistema."""
    def __init__(self, subsistemas: list):
        self._subsistemas = subsistemas
        self._adhierir_a_subsistemas()
        print("[Control Maestro] Observando el sistema...")

    def _adhierir_a_subsistemas(self):
        """Suscribe el controlador a todos los modelos que son Sujetos."""
        for sub in self._subsistemas:
            if isinstance(sub, Subject):
                sub.attach(self)

    # IMPLEMENTACIÓN DE OBSERVER 
    def update(self, subject: Subject, datos_cambio: dict):
        """Método de reaccion del Control Maestro ante cualquier notificacion."""
        nombre_sujeto = subject.__class__.__name__
        evento = datos_cambio.get("evento")

        print(f"\n[CM REACCION] Cambio detectado en {nombre_sujeto}:")

        if evento == "ALARMA_ACTIVADA":
            print(f"  -> ACCION: Se activó una alarma. Bloqueando accesos externos.")
        
        elif evento == "TEMP_CRITICA":
            valor = datos_cambio.get("valor")
            print(f"  -> ACCION: Temperatura de {valor}°C. Activando ventilacion forzada.")
        
        else:
            print(f"  -> ACCION: Evento no reconocido.")

# =================================================================
# 4. DEMOSTRACIÓN DE USO
# =================================================================

# Inicializacion
luces_repo = RepositorioLuces()
luces = LightModel(luces_repo)
temperatura = TempModel()

# Instanciar el Control Maestro (Observador) e inyectar los Sujetos
controlador = ControlMaestro(subsistemas=[luces, temperatura])

print("\n--- SIMULACIÓN DE EVENTOS CRÍTICOS ---")

# A. Evento crítico de Luces
print("\n[Evento A] Activando luz de ALARMA...")
luces.toggle_light("ALARM") # Notifica al controlador

# B. Evento no crítico de Luces
print("\n[Evento B] Apagando luz de ALARMA...")
luces.toggle_light("ALARM") # No notifica (lógica de negocio)

# C. Evento crítico de Temperatura
print("\n[Evento C] La temperatura sube peligrosamente...")
temperatura.temp_actual = 29.0 # Forzamos un valor cercano al umbral
temperatura.medir()            # Esto desencadena la notificacion