from abc import ABC, abstractmethod

# Interfaz de la estrategia para exportar reportes
class ReportExportStrategy(ABC):
    @abstractmethod
    def export(self, data):
        pass

# Estrategias concretas para exportar reportes
class PDFExportStrategy(ReportExportStrategy):
    def export(self, data):
        print(f"Generando reporte en PDF con datos: {data}")

class ExcelExportStrategy(ReportExportStrategy):
    def export(self, data):
        print(f"Generando reporte en Excel con datos: {data}")

class TxtExportStrategy(ReportExportStrategy):
    def export(self, data):
        print(f"Generando reporte en TXT con datos: {data}")

# Contexto del reporte que usa una estrategia para exportar
class Report:
    def __init__(self, data, strategy: ReportExportStrategy):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy: ReportExportStrategy):
        self.strategy = strategy

    def generate_report(self):
        if not self.strategy:
            print("No hay estrategia definida para exportar el reporte.")
        else:
            self.strategy.export(self.data)

# --- Nuevo: Patrón Strategy para descuentos ---

# Interfaz de la estrategia para descuento
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_compra):
        pass

# Estrategias concretas de descuento
class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total_compra):
        descuento = total_compra * 0.05  # 5% descuento
        print(f"Descuento para cliente regular: ${descuento}")
        return total_compra - descuento

class VIPCustomerDiscount(DiscountStrategy):
    def apply_discount(self, total_compra):
        descuento = total_compra * 0.15  # 15% descuento
        print(f"Descuento para cliente VIP: ${descuento}")
        return total_compra - descuento

# Contexto para aplicar descuento
class SalesDiscountContext:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def apply_discount(self, total_compra):
        return self.strategy.apply_discount(total_compra)

# ================== USO DEL STRATEGY ==================
if __name__ == "__main__":
    data = {"ventas": 1500, "gastos": 500, "utilidad": 1000}

    # Reportes con estrategias diferentes
    reporte = Report(data, PDFExportStrategy())
    reporte.generate_report()

    reporte.set_strategy(ExcelExportStrategy())
    reporte.generate_report()

    reporte.set_strategy(TxtExportStrategy())
    reporte.generate_report()

    print("\n--- Aplicando descuentos con Strategy ---")

    # Aplica descuento para cliente regular
    descuento_context = SalesDiscountContext(RegularCustomerDiscount())
    total_con_descuento = descuento_context.apply_discount(1000)
    print(f"Total a pagar: ${total_con_descuento}")

    # Cambiar a descuento para cliente VIP
    descuento_context.set_strategy(VIPCustomerDiscount())
    total_con_descuento = descuento_context.apply_discount(1000)
    print(f"Total a pagar: ${total_con_descuento}")


# =================================================
# Ejemplo adicional: Estrategia en un videojuego para combos de ataque

# Interfaz de la estrategia
class ComboStrategy(ABC):
    @abstractmethod
    def execute_combo(self, player_name):
        pass


# Estrategia concreta: ataque de fuego
class FireCombo(ComboStrategy):
    def execute_combo(self, player_name):
        print(f"{player_name} ejecuta COMBO DE FUEGO : Bola de fuego explosiva!")


# Estrategia concreta: ataque de hielo
class IceCombo(ComboStrategy):
    def execute_combo(self, player_name):
        print(f"{player_name} ejecuta COMBO DE HIELO : Congela al enemigo!")


# Estrategia concreta: ataque de rayo
class LightningCombo(ComboStrategy):
    def execute_combo(self, player_name):
        print(f"{player_name} ejecuta COMBO ELÉCTRICO  : Descarga devastadora!")


# Contexto: jugador
class Player:
    def __init__(self, name, combo_strategy: ComboStrategy):
        self.name = name
        self.combo_strategy = combo_strategy

    def set_combo_strategy(self, combo_strategy: ComboStrategy):
        self.combo_strategy = combo_strategy

    def perform_combo(self):
        if not self.combo_strategy:
            print(f"{self.name} no tiene combo asignado.")
        else:
            self.combo_strategy.execute_combo(self.name)


# ================== USO DEL STRATEGY EN VIDEOJUEGO ==================
if __name__ == "__main__":
    player = Player("Ryu", FireCombo())  # Ryu empieza con el combo de fuego
    player.perform_combo()

    # Cambia el combo a hielo
    player.set_combo_strategy(IceCombo())
    player.perform_combo()

    # Cambia el combo a rayo
    player.set_combo_strategy(LightningCombo())
    player.perform_combo()



