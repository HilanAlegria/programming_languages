# main.py

# --- Importaciones (Mantener __init__.py ayuda aquí) ---
from repositories import HomeRepository
from models import LightsModel, TemperatureModel, WasteModel, BatterySystemModel
from views import HomeViews
from controllers import HomeController
from facade import HomeFacade
from agents import LightAgent, ClimateAgent, EnergyAgent

def initialize_system():
    """Instancia todas las clases y conecta las dependencias (DIP)."""
    print("==============================================")
    print("       INICIALIZANDO SISTEMA DE HOGAR V1      ")
    print("==============================================")
    
    # --- Repositorio (Capa de Acceso a Datos) ---
    repo = HomeRepository()
    
    # --- Modelos (Inyectando el Repositorio) ---
    lights_model = LightsModel(repository=repo)
    temperature_model = TemperatureModel(repository=repo)
    waste_model = WasteModel(repository=repo)
    battery_model = BatterySystemModel(repository=repo)

    # --- Fachada (Inyectando el Repositorio Y Modelos) ---
    facade = HomeFacade(
        repository=repo, # CORRECCIÓN: Inyectar el repo en el Fachada
        lights_model=lights_model,
        temperature_model=temperature_model,
        waste_model=waste_model,
        battery_model=battery_model
    )

    # --- Vistas ---
    views = HomeViews()

    # --- Agentes (Inyectando SOLO el Fachada) ---
    agents = [
        LightAgent(facade=facade), # CORRECCIÓN APLICADA AQUÍ
        ClimateAgent(facade=facade),
        EnergyAgent(facade=facade)
    ]
    print("[INIT] Sistema listo y conectado.")

    # --- Controlador ---
    controller = HomeController(
        facade=facade,
        agents=agents,
        views=views
    )
    
    return controller, repo

# --- 5. Lógica de Simulación de la Aplicación ---
if __name__ == "__main__":
    
    home_controller, home_repo = initialize_system()
    
    # --- SIMULACIÓN 1: ESTADO INICIAL ---
    print("\n--- SIMULACIÓN 1: Verificación del Estado Inicial ---")
    home_controller.handle_request("STATUS_SUMMARY")
    home_controller.show_battery_status()

    # --- SIMULACIÓN 2: ACCIÓN DEL USUARIO ---
    # El usuario apaga la luz de la sala de estar (cambia estado)
    home_controller.handle_request("TOGGLE_LIGHT", {"light_id": "living_room"})
    
    # El usuario activa el modo ausente (acción compleja usando Fachada)
    home_controller.handle_request("SET_AWAY_MODE") # Esto cambia el modo a "Ausente"
    home_controller.handle_request("STATUS_SUMMARY")

    # --- SIMULACIÓN 3: CICLO DE AGENTES ---
    print("\n==============================================")
    print("     INICIANDO CICLO AUTÓNOMO DE AGENTES      ")
    print("==============================================")
    
    for i in range(1, 4):
        print(f"\n>>>> CICLO DE AGENTES NÚMERO {i} <<<<")
        
        if i == 2:
            # Forzamos que la batería al 100% baje (para romper la regla del parcial)
            home_repo.update_battery_charge(1, 95) 
            print(">>> [SIMULADOR] Batería 1 forzada a 95% para romper la regla. <<<")

        home_controller.execute_agent_cycle()

    print("\n--- SIMULACIÓN FINAL: Estado después de ciclos ---")
    home_controller.show_battery_status()
    home_controller.handle_request("STATUS_SUMMARY")