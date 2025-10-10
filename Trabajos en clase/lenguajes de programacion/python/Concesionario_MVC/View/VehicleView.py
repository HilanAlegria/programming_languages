class VehicleView:
    
    def showVehicles(self, vehicles):
        print("\n LISTA DE VEHÍCULOS DISPONIBLES\n")

        if not vehicles:
            print("No se encontraron vehículos con los criterios especificados.\n")
            return

        for v in vehicles:
            print(f"- Tipo: {v['tipo']}")
            print(f"  Marca: {v['marca']}")
            print(f"  Modelo: {v['modelo']}")
            print(f"  Año: {v['año']}")
            print(f"  Precio: ${v['precio']:,}")
            print("-----------------------------")
