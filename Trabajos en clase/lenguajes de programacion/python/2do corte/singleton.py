
# ejercicio: usar el patron de diseño para simular el manejo de sesion de usuario de una platforma de sw
#       con la funcionalidad de autenticacion (login) (simulada) con usuario y contraseña, y (logout).

# (b) FactoryMethod: provee formas de crear objetos en una superclase (interfaz), pero son las subclases las que
#       desiden como crearlos

# (c) Abstract Factory: Permite crear familias de obejtos sin definir sus implementaciones concretas   


class SessionManager:
    _instance_ = None
    _user = None

    def __init__(self):
        raise RuntimeError("Use create_instance para autenticar.")

    @classmethod
    def create_instance(cls, username=None, password=None):
        # Simulación de autenticación (usuario: admin, contraseña: 1234)
        if cls._instance_ is None:
            if username == "admin" and password == "1234":
                cls._instance_ = cls.__new__(cls)
                cls._user = username
            else:
                print("Autenticación fallida.")
                return None
        return cls._instance_

    @classmethod
    def get_user(cls):
        return cls._user

    @classmethod
    def logout(cls):
        cls._instance_ = None
        cls._user = None

# Simulación de uso:
session1 = SessionManager.create_instance("admin", "1234")
session2 = SessionManager.create_instance("admin", "1234")
print(f"¿Es la misma sesión?: {session1 is session2}")
print(f"Usuario autenticado: {SessionManager.get_user()}")

SessionManager.logout()
print(f"Usuario después de logout: {SessionManager.get_user()}")

