from Controller.Vehicle_controller import VehicleController
from View.VehicleView import VehicleView
from Repositories.Vehicle_repository import InMemoryVehicleRepository


if __name__ == "__main__":
    # Instancia del repositorio (modelo de datos simulado en memoria)
    repo = InMemoryVehicleRepository()

    # Instancia de la vista (responsable de mostrar la información)
    view = VehicleView()

    # Instancia del controlador (intermediario entre vista y modelo)
    controller = VehicleController(repo, view)

    # Ejecución de las funciones del controlador
    print("\n=== 🚗 LISTA DE TODOS LOS VEHÍCULOS ===")
    controller.listAllVehicles()

    print("\n=== 🏍️ VEHÍCULOS DE TIPO 'MOTO' ===")
    controller.listByType("Moto")

    print("\n=== 🚛 VEHÍCULOS ENTRE $50,000 Y $150,000 ===")
    controller.listByPriceRange(50000, 150000)
