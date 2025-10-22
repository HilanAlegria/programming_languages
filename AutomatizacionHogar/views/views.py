# views/views.py

class HomeViews:
    """
    Clase que agrupa los métodos de visualización (V) en el patrón MVC.
    Su única responsabilidad es formatear e imprimir los datos.
    """
    
    def __init__(self):
        pass # La vista no requiere dependencias de modelos o repositorios

    def render_summary(self, summary_data):
        """Muestra un resumen conciso del estado global del sistema."""
        print("\n============= REPORTE DE ESTADO DEL HOGAR ==============")
        print(f"Estado Global: {summary_data['Estado Global']}")
        print(f"Luces Encendidas: {summary_data['Luces Encendidas']}")
        print(f"Batería (Regla del 100%): {summary_data['Baterias (Regla 100%)']}")
        print(f"Alerta Residuos: {'SI' if summary_data['Residuos (Alerta)'] else 'NO'}")
        
        clima = summary_data['Clima']
        print(f"Clima Actual: {clima['temperatura_ambiente']}°C (Objetivo: {clima['temperatura_objetivo']}°C)")
        print(f"Estado HVAC: {clima['hvac_estado']}")
        print("========================================================\n")

    def render_light_status(self, light_data):
        """Muestra el estado de una luz específica."""
        if light_data:
            print(f"  > [VISTA] Luz '{light_data['id']}' - Estado: {light_data['estado']}, Intensidad: {light_data['intensidad']}%")
        else:
            print("  > [VISTA] Luz no encontrada.")

    def render_batteries_status(self, batteries_data):
        """Muestra el nivel de carga de todas las baterías."""
        print("\n----------- ESTADO DEL SISTEMA DE BATERÍAS -----------")
        for bat in batteries_data:
            print(f"  ID: {bat['id']} | Tipo: {bat['tipo']} | Carga: {bat['nivel_carga']}% | Estado: {bat['estado']}")
        print("------------------------------------------------------")
        
    def render_waste_levels(self, waste_data):
        """Muestra el nivel de llenado de los contenedores de residuos."""
        print("\n----------- NIVELES DE RESIDUOS -----------")
        for container in waste_data:
            print(f"  Tipo: {container['tipo']} | Llenado: {container['nivel_llenado_porc']}%")
        print("-------------------------------------------")

# NOTA: En main.py, instanciarías:
# views = HomeViews()