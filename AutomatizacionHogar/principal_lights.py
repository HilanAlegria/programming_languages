import random
from abc import ABC, abstractmethod

# =================================================================
# 1. ABSTRACCIÓN DEL PATRÓN OBSERVER
# =================================================================

class Observer(ABC):
    """Interfaz para los Observadores (el Control Maestro)."""
    @abstractmethod
    def update(self, subject: 'Subject', state_data: dict):
        pass

class Subject(ABC):
    """Clase base para los Sujetos (los Subsistemas)."""
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        """Suscribe el observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, state_data: dict):
        """Notifica a todos los observadores de un cambio crítico."""
        print(f"[{self.__class__.__name__}]  Estado crítico cambiado. Notificando...")
        for observer in self._observers:
            observer.update(self, state_data)

# =================================================================
# 2. SUBSISTEMAS (MODELOS/SUJETOS - Cumplen SRP)
# =================================================================

class LightModel(Subject):
    """Modelo de Luces: Solo gestiona el estado de las luces."""
    def __init__(self):
        super().__init__()
        self._state = {"alarma": "OFF"}
    
    def toggle_light(self, light_id: str):
        if light_id in self._state:
            new_state = "ON" if self._state[light_id] == "OFF" else "OFF"
            self._state[light_id] = new_state
            
            # Solo notifica si es un evento crítico (luz de alarma encendida)
            if light_id == "alarma" and new_state == "ON":
                self.notify({"evento": "ALARMA_ACTIVA", "luz": light_id})
            return True
        return False

class TempModel(Subject):
    """Modelo de Temperatura: Solo gestiona mediciones y umbrales."""
    def __init__(self):
        super().__init__()
        self.current_temp = 22.0
        self.alert_threshold = 28.0
        
    def measure_temp(self):
        """Simula un cambio de temperatura y notifica si supera el umbral."""
        self.current_temp += random.uniform(-0.5, 3.0)
        self.current_temp = round(self.current_temp, 1)
        
        if self.current_temp >= self.alert_threshold:
            self.notify({"evento": "SOBRECALENTAMIENTO", "temp": self.current_temp})
        return self.current_temp

# =================================================================
# 3. CONTROL MAESTRO (OBSERVADOR/CONTROLADOR - Cumple SRP/MVC)
# =================================================================

class ControlMaestro(Observer):
    """
    Controlador: Coordina las reacciones.
    Observador: Implementa 'update' para reaccionar a los Sujetos.
    """
    def __init__(self, models: list):
        # Inyección de dependencias de los subsistemas (DIP implícito)
        self.models = models 
        self._subscribe_to_models()
        self.log = []

    def _subscribe_to_models(self):
        """El controlador se suscribe a los modelos observables."""
        for model in self.models:
            if isinstance(model, Subject):
                model.attach(self)
        print("\n[Control Maestro] Suscripción a subsistemas completa.")

    def update(self, subject: Subject, state_data: dict):
        """
        Método de reacción: Se llama cuando un Sujeto notifica.
        Contiene la lógica de acción centralizada.
        """
        subject_name = subject.__class__.__name__
        event = state_data.get("evento")
        
        reaction_msg = f"[CM REACCION]  Cambio en {subject_name} ({event}): "
        
        if event == "ALARMA_ACTIVA":
            light_id = state_data.get("luz")
            reaction_msg += f"Activando sirena y enviando notificacion a seguridad."
            self.log.append("Alarma de Luz Activada")
        
        elif event == "SOBRECALENTAMIENTO":
            temp = state_data.get("temp")
            reaction_msg += f"Temperatura crítica ({temp}°C). Encendiendo AC de emergencia."
            self.log.append(f"Alerta de Temperatura {temp}°C")

        else:
            reaction_msg += "Evento desconocido. Ignorando."

        print(reaction_msg)

# =================================================================
# 4. DEMOSTRACIÓN DE USO
# =================================================================

# Inicialización de Subsistemas (Modelos/Sujetos)
lights_system = LightModel()
temp_system = TempModel()
subsistemas = [lights_system, temp_system]

# Inicialización del Control Maestro (Observador/Controlador)
master_controller = ControlMaestro(subsistemas)

print("\n--- INICIO DE SIMULACIÓN ---")

# EVENTO 1: Un sensor enciende la luz de alarma (CRÍTICO)
print("\n--- Evento 1: Luz de alarma activada ---")
lights_system.toggle_light("alarma") # El Modelo notifica al Controlador

# EVENTO 2: La temperatura sube pero aún no es crítica (NO CRÍTICO)
print("\n--- Evento 2: Mediciones de temperatura normales ---")
for i in range(2):
    temp = temp_system.measure_temp()
    print(f"  > Medición {i+1}: {temp}°C (sin notificación)")

# EVENTO 3: La temperatura cruza el umbral (CRÍTICO)
print("\n--- Evento 3: Temperatura crítica ---")
# Forzamos la temperatura para que cruce el umbral de 28.0
temp_system.current_temp = 27.5
temp_system.measure_temp() # El Modelo notifica al Controlador

print("\n--- LOG DE REACCIONES ---")
print(master_controller.log)