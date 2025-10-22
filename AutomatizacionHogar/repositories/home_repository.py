# repositories/home_repository.py
from .data_simulator import get_document, update_document

class HomeRepository:
    """Clase Repositorio. Aísla a los Modelos de los detalles de la BD (DIP)."""

    # --- Métodos para CONFIGURACIÓN GLOBAL ---
    def get_global_config(self):
        return get_document("configuracion_global")

    def update_global_config(self, new_values):
        return update_document("configuracion_global", None, None, new_values)
    
    # --- Métodos para BATERÍAS ---
    def get_all_batteries(self):
        return get_document("batteries")

    def update_battery_charge(self, battery_id, new_charge_level):
        return update_document(
            collection_name="batteries", 
            search_key="id", 
            search_value=battery_id, 
            new_values={"nivel_carga": new_charge_level}
        )

    # --- Métodos para LUCES ---
    def get_all_lights(self):
        return get_document("lights")

    def update_light_state(self, light_id, new_values):
        return update_document(
            collection_name="lights", 
            search_key="id", 
            search_value=light_id, 
            new_values=new_values
        )

    # --- Métodos para CLIMA ---
    def get_climate_data(self):
        return get_document("climate")

    def update_climate_data(self, new_values):
        return update_document("climate", None, None, new_values)

    # --- Métodos para RESIDUOS ---
    def get_all_waste_containers(self):
        return get_document("waste")

    def update_waste_level(self, waste_type, new_values):
        return update_document(
            collection_name="waste", 
            search_key="tipo", 
            search_value=waste_type, 
            new_values=new_values
        )