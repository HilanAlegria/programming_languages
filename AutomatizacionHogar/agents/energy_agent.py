# agents/energy_agent.py
from agents.agent_control import AgentControl

class EnergyAgent(AgentControl):
    """
    Agente 3: Gestiona la lógica autónoma del sistema de baterías.
    Su función principal es monitorear la regla del 100%.
    """

    def execute_cycle(self):
        """Verifica la regla crítica y simula una acción si no se cumple."""
        
        # 1. Verificar la Regla del Parcial (Lógica de Negocio en el Modelo)
        rule_is_ok = self.facade.battery_model.check_100_percent_rule()
        
        if not rule_is_ok:
            print("    [Agente Energía] ALERTA CRÍTICA: ¡Regla del 100% rota!")
            # 2. Simular Acción Correctiva: Cargar la batería más baja.
            batteries = self.facade.battery_model.get_all_batteries_data()
            if batteries:
                # Encuentra la batería con menor carga
                baja_carga = min(batteries, key=lambda bat: bat['nivel_carga'])
                
                # Simula una carga forzada (ej. +20%)
                charge_rate = 20 
                self.facade.battery_model.simulate_charge_cycle(baja_carga['id'], charge_rate)
                
                print(f"    [Agente Energía] Acción Correctiva: Iniciando carga (+{charge_rate}%) en Batería ID {baja_carga['id']} ({baja_carga['nivel_carga']}%).")
        else:
            # Simular descarga normal para todas las baterías (simulación de uso)
            for bat in self.facade.battery_model.get_all_batteries_data():
                self.facade.battery_model.simulate_charge_cycle(bat['id'], -5) # Simula una descarga -5%
            print("    [Agente Energía] Regla OK. Simulación: Descarga pasiva del sistema (-5% a todas).")


    def report_status(self):
        if self.facade.battery_model.check_100_percent_rule():
            return "Estado: Óptimo. La regla del 100% se cumple."
        else:
            return "Estado: Crítico. Se requiere carga."