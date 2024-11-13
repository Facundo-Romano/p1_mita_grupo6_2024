def convertir_a_lista(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return { clave: convertir_a_lista(valor) for clave, valor in obj.items() }
    #PENDIENTE: Chequear
    elif isinstance(obj, list):
        return [convertir_a_lista(item) for item in obj]
    else:
        return obj
