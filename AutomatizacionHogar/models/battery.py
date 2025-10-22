# models/battery.py
from abc import ABC, abstractmethod

# --- PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP) ---
class Battery(ABC):
    """Clase base abstracta para cualquier tipo de batería."""
    
    def __init__(self, battery_id, carga, tipo):
        self.id = battery_id
        self.nivel_carga = carga
        self.tipo = tipo

    @abstractmethod
    def get_max_charge_rate(self):
        """Define la tasa máxima de carga (diferente para cada subtipo)."""
        pass

# Clases concretas que son sustituibles
class LithiumBattery(Battery):
    def __init__(self, battery_id, carga):
        super().__init__(battery_id, carga, "Litio")
    
    def get_max_charge_rate(self):
        return 15  # Carga rápida

class LeadAcidBattery(Battery):
    def __init__(self, battery_id, carga):
        super().__init__(battery_id, carga, "Plomo")
    
    def get_max_charge_rate(self):
        return 5  # Carga lenta

# ---------------------------------------------------

class BatterySystemModel:
    """
    Modelo para la gestión del sistema de baterías.
    Contiene la Lógica de Negocio, incluyendo la regla del parcial.
    """
    
    def __init__(self, repository):
        self.repository = repository

    def get_all_batteries_data(self):
        """Obtiene la lista de baterías del Repositorio."""
        return self.repository.get_all_batteries()
        
    def check_100_percent_rule(self):
        """
        Lógica de Negocio CRÍTICA (Regla del Parcial): 
        Verifica si al menos una batería está cargada al 100%.
        """
        batteries_data = self.get_all_batteries_data() 
        
        for bat_doc in batteries_data:
            if bat_doc.get("nivel_carga") == 100:
                print("  -> [Baterías Lógica] REGLA CUMPLIDA: Una batería está al 100%.")
                return True
        
        print("  -> [Baterías Lógica] ALERTA CRÍTICA: NINGUNA batería está al 100%.")
        return False

    def simulate_charge_cycle(self, battery_id, rate):
        """Simula la carga o descarga de una batería y actualiza el Repositorio."""
        
        batteries_data = self.get_all_batteries_data()
        
        for doc in batteries_data:
            if doc.get("id") == battery_id:
                # Aplicar la lógica de carga/descarga
                nueva_carga = doc["nivel_carga"] + rate
                if nueva_carga > 100: nueva_carga = 100
                if nueva_carga < 0: nueva_carga = 0
                
                # Actualizar el estado en el Repositorio (simulación de BD)
                self.repository.update_battery_charge(battery_id, nueva_carga)
                return True
        return False