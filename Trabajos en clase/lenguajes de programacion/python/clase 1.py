class Paradigma:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def mostrar_info(self):
        print(f"Paradigma: {self.nombre}")
        print(f"Descripción: {self.descripcion}")

# Ejemplo de uso
if __name__ == "__main__":
    paradigma = Paradigma("Orientado a Objetos", "Organiza el software en objetos que interactúan entre sí.")
    paradigma.mostrar_info()