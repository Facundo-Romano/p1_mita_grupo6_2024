def obtener_numero(texto, min, max):
    try:   
        numero = int(input(texto))

        while numero < min or numero > max:
            numero = input(texto)
        
        return numero
    except Exception as e:
        print("Por favor ingrese un número válido")
        return obtener_numero(texto, min, max)
