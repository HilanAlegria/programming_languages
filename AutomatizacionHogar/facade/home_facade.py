# facade/home_facade.py

class HomeFacade:
    """
    Patrón Fachada: Proporciona una interfaz simplificada (ISP) para interactuar 
    con los subsistemas complejos (los Modelos).
    """

    def __init__(self, repository, lights_model, temperature_model, waste_model, battery_model):
        # Inyecta el Repositorio para acceder a datos globales (como el modo)
        self.repository = repository 
        
        # Subsistemas (Modelos)
        self.lights_model = lights_model
        self.temperature_model = temperature_model
        self.waste_model = waste_model
        self.battery_model = battery_model

    # --- Nuevo método para Agentes (DIP) ---
    def get_global_config(self):
        """Método de Fachada para acceder a la configuración global (modo)."""
        return self.repository.get_global_config()

    # --- Métodos de Alto Nivel para el Controlador ---
    def set_away_mode(self):
        """Establece el modo 'Ausente' (Away Mode) y coordina subsistemas."""
        print("\n[FACADE] Activando Modo 'Ausente'...")
        
        # 1. Actualizar el estado global
        self.repository.update_global_config({"modo_actual": "Ausente"})
        
        # 2. Ajustar luces (delegando al Modelo)
        all_lights = self.lights_model.get_all_lights()
        for light in all_lights:
            if light['estado'] == "Encendida":
                self.lights_model.toggle_light(light['id'], new_state="Apagada")
        print("  -> Todas las luces han sido apagadas.")
        
        # 3. Ajustar temperatura objetivo
        self.temperature_model.set_target_temperature(18.0)
        print("  -> Temperatura objetivo ajustada a 18.0°C.")
        
        # 4. Verificar estado crítico de energía
        if not self.battery_model.check_100_percent_rule():
            print("  -> ALERTA: La regla de la batería no se cumple. El agente de energía debe tomar acción.")
        
        return "Modo Ausente activado con éxito."

    def get_system_status_summary(self):
        """Obtiene un resumen completo del estado del hogar."""
        battery_ok = self.battery_model.check_100_percent_rule()
        config = self.get_global_config()
        
        summary = {
            "Modo Actual": config.get("modo_actual"),
            "Estado Global": "Óptimo" if battery_ok else "ALERTA ENERGÍA",
            "Luces Encendidas": len([l for l in self.lights_model.get_all_lights() if l['estado'] == "Encendida"]),
            "Clima": self.temperature_model.get_climate_data(),
            "Baterias (Regla 100%)": "Cumplida" if battery_ok else "Fallida",
            "Residuos (Alerta)": self.waste_model.check_for_collection()
        }
        return summary

    # --- Métodos Simples (Delegación Directa) ---
    def toggle_light(self, light_id):
        return self.lights_model.toggle_light(light_id)
        
    def check_waste_collection(self):
        return self.waste_model.check_for_collection()