from Concesionario_MVC.Repositories import VehicleRepository

# Se aplica la "O" de SOLID (Open/Closed): esta clase concreta extiende la abstracción sin modificarla.
class MongoDBRepository(VehicleRepository):
    
    def get_all(self):
        # Simulación de datos en una "base de datos" MongoDB
        return [
            {"tipo": "Auto", "marca": "Toyota", "modelo": "Corolla", "año": 2022, "precio": 80000},
            {"tipo": "Camion", "marca": "Volvo", "modelo": "FH16", "año": 2020, "precio": 350000},
            {"tipo": "Moto", "marca": "Yamaha", "modelo": "MT-07", "año": 2023, "precio": 40000},
            {"tipo": "Auto", "marca": "Mazda", "modelo": "CX-5", "año": 2021, "precio": 95000},
            {"tipo": "Moto", "marca": "Suzuki", "modelo": "GSX-R1000", "año": 2024, "precio": 120000},
        ]
