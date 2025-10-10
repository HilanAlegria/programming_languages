from abc import ABC, abstractmethod

class VehicleRepository(ABC):
    
    @abstractmethod
    def get_all(self):
        pass

class IReadableRepository(ABC):
    
    @abstractmethod
    def read_all(self):
        pass


class IWritableRepository(ABC):
    
    @abstractmethod
    def save_item(self, item):
        pass


class InMemoryVehicleRepository(VehicleRepository):
    
    def __init__(self):
        # Base de datos simulada (lista de diccionarios)
        self.vehicles = [
            {"tipo": "Auto", "marca": "Toyota", "modelo": "Corolla", "año": 2022, "precio": 80000},
            {"tipo": "Camion", "marca": "Volvo", "modelo": "FH16", "año": 2020, "precio": 350000},
            {"tipo": "Moto", "marca": "Yamaha", "modelo": "MT-07", "año": 2023, "precio": 40000},
            {"tipo": "Auto", "marca": "Mazda", "modelo": "CX-5", "año": 2021, "precio": 95000},
        ]
    
    # Obtener todos los vehículos
    def get_all(self):
        return self.vehicles

    # Filtrar por tipo de vehículo
    def get_by_type(self, tipo: str):
        return [v for v in self.vehicles if v["tipo"].lower() == tipo.lower()]

    # Filtrar por rango de precios
    def get_by_price_range(self, precio_min: float, precio_max: float):
        return [v for v in self.vehicles if precio_min <= v["precio"] <= precio_max]

    # (opcional) Guardar un nuevo vehículo
    def save_item(self, vehicle):
        self.vehicles.append(vehicle)
