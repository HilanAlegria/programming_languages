# agents/light_agent.py
from .agent_control import AgentControl

class LightAgent(AgentControl):
    """Agente 1: Gestiona la lógica autónoma de las luces."""
    
    def __init__(self, facade):
        super().__init__(facade)
        # YA NO SE NECESITA EL REPOSITORIO

    def execute_cycle(self):
        """Verifica el modo del hogar y apaga las luces innecesarias."""
        
        # ACCEDE AL MODO GLOBAL A TRAVÉS DEL FACHADA (DIP OK)
        home_config = self.facade.get_global_config() 
        
        if home_config.get("modo_actual") == "Ausente":
            lights_data = self.facade.lights_model.get_all_lights()
            
            lights_off_count = 0
            for light in lights_data:
                if light['estado'] == "Encendida":
                    self.facade.lights_model.toggle_light(light['id'], new_state="Apagada")
                    lights_off_count += 1
            
            if lights_off_count > 0:
                print(f"    [Agente Luces] Modo 'Ausente' detectado. Apagó {lights_off_count} luces.")
            else:
                print("    [Agente Luces] Modo 'Ausente' detectado. No había luces encendidas.")

    def report_status(self):
        config = self.facade.get_global_config()
        return f"Estado: Listo. Modo actual: {config['modo_actual']}."