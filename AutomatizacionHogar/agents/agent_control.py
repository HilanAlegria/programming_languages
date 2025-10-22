# agents/agent_control.py
from abc import ABC, abstractmethod

class AgentControl(ABC):
    """
    Clase base abstracta (interfaz) para todos los agentes de control.
    Cumple con el Principio de Inversión de Dependencia (DIP):
    El controlador depende de esta abstracción, no de los agentes concretos.
    """
    def __init__(self, facade):
        self.facade = facade  # Inyección del Fachada para interactuar con el sistema

    @abstractmethod
    def execute_cycle(self):
        """Método principal para ejecutar la lógica autónoma del agente."""
        pass

    @abstractmethod
    def report_status(self):
        """Método para que el agente reporte su estado o acciones tomadas."""
        pass