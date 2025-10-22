# repositories/data_simulator.py
import copy

# --- SIMULACIÓN DE LA BASE DE DATOS (DOCUMENTOS ESTÁTICOS) ---
DATOS_HOGAR = {
    "configuracion_global": {
        "nombre": "Casa Inteligente Beta",
        "direccion": "Calle Falsa 123",
        "modo_actual": "Presente" # Estado inicial
    },
    "batteries": [
        {"id": 1, "tipo": "Litio", "nivel_carga": 100, "estado": "Cargando", "prioridad": "Alta"},
        {"id": 2, "tipo": "Plomo", "nivel_carga": 45, "estado": "Descargando", "prioridad": "Baja"},
    ],
    "lights": [
        {"id": "living_room", "estado": "Encendida", "intensidad": 80},
        {"id": "kitchen", "estado": "Apagada", "intensidad": 0}
    ],
    "climate": {
        "temperatura_ambiente": 25.5,
        "temperatura_objetivo": 22.0,
        "hvac_estado": "Apagado"
    },
    "waste": [
        {"tipo": "Organico", "nivel_llenado_porc": 75},
        {"tipo": "Plastico", "nivel_llenado_porc": 20}
    ]
}

# --- FUNCIONES DE ACCESO SIMULADO ---
def get_document(collection_name):
    """Simula una consulta SELECT."""
    return copy.deepcopy(DATOS_HOGAR.get(collection_name))

def update_document(collection_name, search_key, search_value, new_values):
    """Simula una consulta UPDATE."""
    
    if collection_name in ["configuracion_global", "climate"]:
        DATOS_HOGAR[collection_name].update(new_values)
        return True

    collection = DATOS_HOGAR.get(collection_name)
    if collection and isinstance(collection, list):
        for doc in collection:
            if doc.get(search_key) == search_value:
                doc.update(new_values)
                return True
    
    return False