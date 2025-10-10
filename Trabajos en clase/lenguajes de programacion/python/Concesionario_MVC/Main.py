from Controller.Vehicle_controller import VehicleController
from View.VehicleView import VehicleView
from Repositories.mongodb_repository import MongoDBRepository   # <── usamos la BD simulada


if __name__ == "__main__":
    # Instanciamos la "base de datos" MongoDB simulada
    repo = MongoDBRepository()

    # Vista y controlador
    view = VehicleView()
    controller = VehicleController(repo, view)

    # Llamadas de prueba
    print("\n===  LISTA DE TODOS LOS VEHÍCULOS ===")
    controller.listAllVehicles()

    print("\n===  VEHÍCULOS DE TIPO 'MOTO' ===")
    controller.listByType("Moto")

    print("\n===  VEHÍCULOS ENTRE $50,000 Y $150,000 ===")
    controller.listByPriceRange(50000, 150000)
