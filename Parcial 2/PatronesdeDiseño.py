class ControlMaestro:
    """Implementa el patrón Singleton para el Control Maestro del sistema.
    Asegura que solo exista una instancia de esta clase."""
    # Variable de clase para almacenar la única instancia
    _instancia = None
    # Atributo para controlar si la inicialización ya se ha ejecutado
    _inicializado = False

    def __new__(cls, *args, **kwargs):
        """
        Método mágico que se llama antes de __init__ para crear la instancia.
        Controla que solo se cree una vez.
        """
        # Si no hay instancia, la crea. Si ya existe, devuelve la existente.
        if cls._instancia is None:
            # Llama al método __new__ de la clase base (object) para crear la instancia
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        """
        Inicializa la instancia solo una vez.
        """
        if not self._inicializado:
            print("Control Maestro: Inicializando el sistema...")
            # Aquí se inicializan los subsistemas o recursos principales
            self.subsistema_a = "Subsistema A: En línea"
            self.subsistema_b = "Subsistema B: En línea"
            self._inicializado = True
            print("Control Maestro: Inicialización completa.")
        else:
            # Este mensaje se imprime si se intenta inicializar una instancia ya existente
            print("Control Maestro: La instancia ya está inicializada.")

    def obtener_estado_subsistemas(self):
        """
        Método para obtener el estado actual de los subsistemas controlados.
        """
        print("\n--- Estado de los Subsistemas ---")
        print(f"Estado A: {self.subsistema_a}")
        print(f"Estado B: {self.subsistema_b}")

    def iniciar_operacion(self):
        """
        Método de ejemplo para simular una operación de control.
        """
        print("\nControl Maestro: Iniciando operación central.")
        # Lógica de control de los subsistemas
        print("Control Maestro: Verificando permisos y secuencias.")
        print("Control Maestro: Desplegando subsistemas.")

# --- Ejemplo de Uso ---

# 1. Intentamos crear la primera instancia del Control Maestro
print("Intento 1: Creando el Control Maestro...")
control1 = ControlMaestro()
control1.obtener_estado_subsistemas()
control1.iniciar_operacion()

print("-" * 30)

# 2. Intentamos crear una segunda instancia
# Python devolverá la misma instancia que 'control1'
print("Intento 2: Intentando crear otra instancia del Control Maestro...")
control2 = ControlMaestro()
# Aunque se llama al constructor, la inicialización solo ocurre una vez

# 3. Verificación de que son la misma instancia
print("-" * 30)
print(f"¿Son control1 y control2 la misma instancia? {control1 is control2}")
print(f"ID de control1: {id(control1)}")
print(f"ID de control2: {id(control2)}")

# 4. Modificamos un estado usando una referencia y vemos el cambio en la otra
print("\nControl Maestro: Modificando el estado del Subsistema B (a través de control1)")
control1.subsistema_b = "Subsistema B: Mantenimiento programado"
control2.obtener_estado_subsistemas() # control2 refleja el cambio hecho por control1