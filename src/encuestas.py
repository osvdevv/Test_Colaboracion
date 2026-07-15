"""
Módulo de encuestas.

Implementa funciones para analizar respuestas usando listas y diccionarios.
"""


def contar_respuestas(respuestas):
    return len(respuestas)


def obtener_opciones(respuestas):
    opciones = []
    for respuesta in respuestas:
        if respuesta not in opciones:
            opciones.append(respuesta)
    return opciones


def frecuencia_respuestas(respuestas):
    frecuencias = {}
    for respuesta in respuestas:
        if respuesta in frecuencias:
            frecuencias[respuesta] += 1
        else:
            frecuencias[respuesta] = 1
    return frecuencias

def respuesta_mas_comun(respuestas):
    if not respuestas:
        return None
        
    frecuencias = frecuencia_respuestas(respuestas)
    mas_comun = None
    max_frecuencia = -1

    for respuesta, frec in frecuencias.items():
        if frec > max_frecuencia:
            max_frecuencia = frec
            mas_comun = respuesta
            
    return mas_comun


def porcentaje_respuesta(respuestas, opcion):
    if not respuestas:
        return 0.0
        
    total = contar_respuestas(respuestas)
    conteo_opcion = respuestas.count(opcion)
    
    return (conteo_opcion / total) * 100


def resumen_encuesta(respuestas):
    if not respuestas:
        return {
            "total": 0,
            "opciones": [],
            "frecuencias": {},
            "mas_comun": None
        }
        
    return {
        "total": contar_respuestas(respuestas),
        "opciones": obtener_opciones(respuestas),
        "frecuencias": frecuencia_respuestas(respuestas),
        "mas_comun": respuesta_mas_comun(respuestas)
    }
