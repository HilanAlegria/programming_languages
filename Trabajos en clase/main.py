import getpass

# Base de datos simulada en memoria
usuarios = {}
vuelos = [
    {
        "codigo": "AV101",
        "origen": "Madrid",
        "destino": "Barcelona",
        "fecha": "2025-10-15",
        "hora": "10:00",
        "tarifa": 120,
        "asientos_disponibles": 5,
        "info": "Vuelo directo"
    },
    {
        "codigo": "AV202",
        "origen": "Madrid",
        "destino": "Paris",
        "fecha": "2025-10-16",
        "hora": "15:30",
        "tarifa": 150,
        "asientos_disponibles": 3,
        "info": "Vuelo con escala en Lyon"
    }
]

reservas = {}

def registrar():
    print("registro de usuario")
    while True:
        username = input("Email: ")
        if username in usuarios:
            print("El usuario ya existe")
        else:
            break
    password = getpass.getpass("Contraseña: ")
    usuarios[username] = password
    print("Registro exitoso. Ya puedes iniciar sesión.")

def iniciar_sesion():
    print("=== Inicio de Sesión ===")
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")
    if usuarios.get(username) == password:
        print(f"Bienvenido {username}!")
        print("Servicios disponibles: Consultar vuelos, Reservar, Comprar billetes, Ver horarios, Información de vuelos.")
        return username
    else:
        print("Usuario o contraseña incorrectos.")
        return None

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Consultar vuelos")
    print("2. Reservar vuelo")
    print("3. Comprar billete")
    print("4. Ver horarios y tarifas")
    print("5. Información de un vuelo")
    print("6. Cerrar sesión")

def consultar_vuelos():
    origen = input("Origen: ").capitalize()
    destino = input("Destino: ").capitalize()
    fecha = input("Fecha (YYYY-MM-DD): ")
    encontrados = [v for v in vuelos if v["origen"] == origen and v["destino"] == destino and v["fecha"] == fecha]
    if encontrados:
        print("Vuelos encontrados:")
        for v in encontrados:
            print(f"Código: {v['codigo']}, Hora: {v['hora']}, Tarifa: {v['tarifa']}€, Asientos disponibles: {v['asientos_disponibles']}")
    else:
        print("No se encontraron vuelos para esa ruta y fecha.")

def reservar_vuelo(usuario):
    codigo = input("Código del vuelo a reservar: ").upper()
    vuelo = next((v for v in vuelos if v["codigo"] == codigo), None)
    if vuelo:
        if vuelo["asientos_disponibles"] > 0:
            reservas.setdefault(usuario, []).append(codigo)
            vuelo["asientos_disponibles"] -= 1
            print(f"Reserva realizada para el vuelo {codigo}.")
        else:
            print("No quedan asientos disponibles en ese vuelo.")
    else:
        print("Código de vuelo no válido.")

def comprar_billete(usuario):
    if usuario not in reservas or len(reservas[usuario]) == 0:
        print("No tienes reservas para comprar billete.")
        return
    print("Tus reservas:")
    for i, codigo in enumerate(reservas[usuario], 1):
        print(f"{i}. {codigo}")
    opcion = int(input("Selecciona la reserva que quieres comprar (número): "))
    if 1 <= opcion <= len(reservas[usuario]):
        codigo = reservas[usuario].pop(opcion - 1)
        print(f"Compra realizada para el vuelo {codigo}. ¡Buen viaje!")
    else:
        print("Opción inválida.")

def ver_horarios_tarifas():
    print("Horarios y tarifas de vuelos disponibles:")
    for v in vuelos:
        print(f"{v['codigo']}: {v['origen']} -> {v['destino']} el {v['fecha']} a las {v['hora']}, Precio: {v['tarifa']}€")

def informacion_vuelo():
    codigo = input("Ingrese el código del vuelo: ").upper()
    vuelo = next((v for v in vuelos if v["codigo"] == codigo), None)
    if vuelo:
        print(f"Información del vuelo {codigo}:")
        print(f"Ruta: {vuelo['origen']} -> {vuelo['destino']}")
        print(f"Fecha: {vuelo['fecha']}")
        print(f"Hora: {vuelo['hora']}")
        print(f"Tarifa: {vuelo['tarifa']}€")
        print(f"Asientos disponibles: {vuelo['asientos_disponibles']}")
        print(f"Detalles: {vuelo['info']}")
    else:
        print("Código de vuelo no encontrado.")

def main():
    print("¡Bienvenido al Sistema de Reserva de Vuelos!")
    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                while True:
                    mostrar_menu_principal()
                    opcion_usuario = input("Elige una opción: ")
                    if opcion_usuario == "1":
                        consultar_vuelos()
                    elif opcion_usuario == "2":
                        reservar_vuelo(usuario)
                    elif opcion_usuario == "3":
                        comprar_billete(usuario)
                    elif opcion_usuario == "4":
                        ver_horarios_tarifas()
                    elif opcion_usuario == "5":
                        informacion_vuelo()
                    elif opcion_usuario == "6":
                        print("Cerrando sesión...")
                        break
                    else:
                        print("Opción no válida.")

if __name__ == "__main__":
    main()
