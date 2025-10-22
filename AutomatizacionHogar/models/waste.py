# models/waste.py

class WasteModel:
    """
    Modelo para la gestión de los niveles de residuos.
    Responsabilidad Única (SRP): Solo se encarga de la lógica de residuos.
    """
    
    def __init__(self, repository):
        self.repository = repository

    def get_waste_levels(self):
        """Obtiene los niveles de llenado de todos los contenedores."""
        return self.repository.get_all_waste_containers()

    def check_for_collection(self):
        """Lógica de negocio: verifica si algún contenedor necesita recolección."""
        containers = self.get_waste_levels()
        for container in containers:
            if container['nivel_llenado_porc'] >= 85:
                # Simulación de una alerta o notificación
                print(f"  -> [Residuos Lógica] ALERTA: Contenedor '{container['tipo']}' requiere recolección ({container['nivel_llenado_porc']}%).")
                return True
        return False

    def empty_container(self, waste_type):
        """Simula el vaciado de un contenedor (pone el nivel a 0)."""
        self.repository.update_waste_level(waste_type, {"nivel_llenado_porc": 0})
        print(f"  -> [Residuos Lógica] Contenedor '{waste_type}' vaciado y actualizado en el sistema.")