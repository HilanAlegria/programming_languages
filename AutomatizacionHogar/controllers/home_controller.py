# controllers/home_controller.py

class HomeController:
    """
    Controlador principal (C) en el patrón MVC.
    
    Responsabilidades (SRP):
    1. Recibir peticiones del "usuario" (simulado por main.py).
    2. Usar la Fachada para ejecutar la lógica de negocio.
    3. Ejecutar el ciclo de los agentes de control autónomo.
    4. Seleccionar la Vista para presentar los resultados.
    """
    
    def __init__(self, facade, agents, views):
        # Inyección de dependencias (DIP)
        self.facade = facade       # Abstracción sobre la lógica de negocio compleja
        self.agents = agents       # Lista de objetos AgenteControl (depende de la abstracción)
        self.views = views         # Vistas disponibles (para renderizar)

    # --- Métodos de Gestión de Peticiones del Usuario (Capa de Entrada) ---

    def handle_request(self, action, data=None):
        """Maneja las peticiones simuladas del usuario."""
        
        print(f"\n[CONTROLADOR] Procesando acción: '{action}'")
        
        if action == "STATUS_SUMMARY":
            summary = self.facade.get_system_status_summary()
            self.views.render_summary(summary)

        elif action == "SET_AWAY_MODE":
            result = self.facade.set_away_mode()
            print(f"[CONTROLADOR] Resultado: {result}")
        
        elif action == "TOGGLE_LIGHT":
            light_id = data.get("light_id")
            if self.facade.toggle_light(light_id):
                print(f"[CONTROLADOR] Luz '{light_id}' actualizada. Nuevo estado:")
                self.views.render_light_status(self.facade.lights_model.get_light_state(light_id))
            else:
                print(f"[CONTROLADOR] Error: Luz '{light_id}' no encontrada.")

        else:
            print(f"[CONTROLADOR] Advertencia: Acción '{action}' no reconocida.")

    # --- Método de Gestión de Agentes (Lógica de Fondo) ---

    def execute_agent_cycle(self):
        """
        Ejecuta el ciclo de los 3 agentes autónomos.
        """
        print("\n--- INICIO CICLO AGENTES AUTÓNOMOS ---")
        for agent in self.agents:
            # Los agentes deben implementar el contrato de AgenteControl (ISP)
            print(f"  > Agente: {agent.__class__.__name__}")
            agent.execute_cycle()
        print("--- FIN CICLO AGENTES AUTÓNOMOS ---\n")
        
    # --- Métodos de Presentación (Delegación a Vistas) ---

    def show_battery_status(self):
        """Muestra el estado de la batería usando la Vista de Baterías."""
        battery_data = self.facade.battery_model.get_all_batteries_data()
        self.views.render_batteries_status(battery_data)
        self.facade.battery_model.check_100_percent_rule()