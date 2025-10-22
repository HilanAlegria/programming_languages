# models/lights.py

class LightsModel:
    """
    Modelo para la gestión del estado de las luces.
    Responsabilidad Única (SRP): Solo se encarga de la lógica de luces.
    """
    
    def __init__(self, repository):
        # Inyección de dependencia (DIP)
        self.repository = repository

    def get_light_state(self, light_id):
        """Obtiene el estado actual de una luz por ID."""
        lights = self.repository.get_all_lights()
        for light in lights:
            if light['id'] == light_id:
                return light
        return None

    def toggle_light(self, light_id, new_state=None):
        """Cambia el estado de una luz (Encendida/Apagada)."""
        current_state = self.get_light_state(light_id)
        if current_state:
            # Lógica para determinar el nuevo estado
            if new_state is None:
                new_state = "Apagada" if current_state['estado'] == "Encendida" else "Encendida"
            
            # Persistir el cambio a través del Repositorio
            self.repository.update_light_state(light_id, {"estado": new_state})
            return True
        return False

    def get_all_lights(self):
        """Retorna el estado de todas las luces."""
        return self.repository.get_all_lights()