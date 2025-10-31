# controllers/home_controller.py

class HomeController:
    """
    Controlador principal (C) en el patrón MVC, implementado como SINGLETON.
    Asegura que solo una instancia controle el sistema completo.
    """
    
    # ------------------- IMPLEMENTACIÓN SINGLETON -------------------
    _instancia = None
    _inicializado = False 

    def __new__(cls, *args, **kwargs):
        """
        Método de control de creación. Si no hay instancia, la crea. 
        Si ya existe, devuelve la existente.
        """
        if cls._instancia is None:
            # Llama al __new__ de la clase base para crear el objeto
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, facade=None, agents=None, views=None):
        """
        Inicializa la instancia solo la primera vez, manteniendo la Inyección de Dependencias (DIP).
        """
        if not self._inicializado:
            print("[CM Singleton] Inicializando el Control Maestro con dependencias...")
            # Inyección de dependencias (DIP) - Se guarda solo en la primera inicialización
            self.facade = facade       # Abstracción sobre la lógica de negocio compleja
            self.agents = agents       # Lista de objetos AgenteControl
            self.views = views         # Vistas disponibles
            self._inicializado = True
            print("[CM Singleton] Inicialización completa.")
        else:
            # Si ya está inicializado, no se modifican las dependencias
            pass 
    # ----------------------------------------------------------------

    # --- Métodos de Gestión de Peticiones del Usuario (Capa de Entrada) ---

    def handle_request(self, action, data=None):
        # Es buena práctica verificar si las dependencias se inyectaron correctamente
        if not self._inicializado or self.facade is None:
            print("[CM ERROR] El controlador no ha sido inicializado correctamente.")
            return

        print(f"\n[CONTROLADOR] Procesando acción: '{action}'")
        
        # ... (El resto de la lógica de handle_request se mantiene igual)
        if action == "STATUS_SUMMARY":
            summary = self.facade.get_system_status_summary()
            self.views.render_summary(summary)

        # ... (Se omiten los demás elif para brevedad) ...

        elif action == "TOGGLE_LIGHT":
            light_id = data.get("light_id") if data else None
            if light_id and self.facade.toggle_light(light_id):
                 print(f"[CONTROLADOR] Luz '{light_id}' actualizada. Nuevo estado:")
                 # Aquí necesitas asegurarte de que facade tiene un método para obtener el estado, 
                 # o que lights_model fue inyectado en facade.
                 # Usaremos el acceso a través de facade, asumiendo que tiene la referencia al modelo
                 self.views.render_light_status(self.facade.get_light_state(light_id))
            else:
                 print(f"[CONTROLADOR] Error: Luz '{light_id}' no encontrada o ID nulo.")


    # --- Método de Gestión de Agentes (Lógica de Fondo) ---

    def execute_agent_cycle(self):
        """
        Ejecuta el ciclo de los 3 agentes autónomos.
        """
        # ... (Lógica que se mantiene igual) ...
        if not self.agents:
            print("No hay agentes configurados.")
            return

        print("\n--- INICIO CICLO AGENTES AUTÓNOMOS ---")
        for agent in self.agents:
            print(f" > Agente: {agent.__class__.__name__}")
            agent.execute_cycle()
        print("--- FIN CICLO AGENTES AUTÓNOMOS ---\n")
    # ... (Otros métodos se mantienen igual) ...