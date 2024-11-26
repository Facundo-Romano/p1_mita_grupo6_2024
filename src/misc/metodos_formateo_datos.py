def convertir_a_lista(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return { clave: convertir_a_lista(valor) for clave, valor in obj.items() }
    else:
        return obj
