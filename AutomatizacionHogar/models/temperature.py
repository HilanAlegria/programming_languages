# models/temperature.py

class TemperatureModel:
    """
    Modelo para la gestión del control de temperatura (clima).
    Responsabilidad Única (SRP): Solo se encarga de la lógica de temperatura.
    """
    
    def __init__(self, repository):
        self.repository = repository

    def get_climate_data(self):
        """Obtiene todos los datos de clima (ambiente, objetivo, HVAC)."""
        # El repositorio retorna un solo documento/diccionario para el clima
        return self.repository.get_climate_data()

    def set_target_temperature(self, new_temp):
        """Establece la temperatura objetivo deseada."""
        if 18.0 <= new_temp <= 30.0:  # Lógica de negocio de validación
            self.repository.update_climate_data({"temperatura_objetivo": new_temp})
            return True
        return False

    def adjust_hvac_state(self, current_temp):
        """Lógica para encender o apagar el HVAC según la temperatura objetivo."""
        data = self.get_climate_data()
        target = data['temperatura_objetivo']
        hvac_state = data['hvac_estado']
        
        new_hvac_state = hvac_state
        
        if current_temp < target - 1:
            new_hvac_state = "Calefaccion"
        elif current_temp > target + 1:
            new_hvac_state = "Aire Acondicionado"
        elif abs(current_temp - target) <= 0.5:
            new_hvac_state = "Apagado"

        if new_hvac_state != hvac_state:
            self.repository.update_climate_data({"hvac_estado": new_hvac_state})
            print(f"  -> [Temp. Lógica] HVAC ajustado a: {new_hvac_state}")
        
        return new_hvac_state