# Aplicando el principio S de SOLID:
# Esta clase solo se encarga de representar los datos de un vehículo.

class Vehicle:
    
    def __init__(self, tipo: str, marca: str, modelo: str, año: int, precio: float):
        self.tipo = tipo          # Ej: "Auto", "Camion", "Moto"
        self.marca = marca        # Ej: "Toyota"
        self.modelo = modelo      # Ej: "Corolla"
        self.año = año            # Ej: 2023
        self.precio = precio      # Ej: 50000.0
