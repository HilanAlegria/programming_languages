# agents/climate_agent.py
from agents.agent_control import AgentControl

class ClimateAgent(AgentControl):
    """
    Agente 2: Gestiona la lógica autónoma del clima.
    """

    def execute_cycle(self):
        """Verifica la temperatura actual y ajusta el HVAC si es necesario."""
        
        # Simulación: obtenemos la temperatura ambiente y la temperatura objetivo
        climate_data = self.facade.temperature_model.get_climate_data()
        current_temp = climate_data['temperatura_ambiente']
        target_temp = climate_data['temperatura_objetivo']
        
        # Lógica de ajuste del HVAC (delegamos la lógica al Modelo para SRP)
        new_hvac_state = self.facade.temperature_model.adjust_hvac_state(current_temp)
        
        if new_hvac_state != climate_data['hvac_estado']:
            print(f"    [Agente Clima] Tarea: Ajuste HVAC a '{new_hvac_state}' (Actual: {current_temp}°C, Obj: {target_temp}°C).")
        else:
            print(f"    [Agente Clima] Tarea: Temperatura estable ({current_temp}°C). HVAC: {new_hvac_state}.")


    def report_status(self):
        data = self.facade.temperature_model.get_climate_data()
        return f"Estado: Operando. HVAC en {data['hvac_estado']}."