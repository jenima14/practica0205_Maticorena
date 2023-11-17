def area_del_circulo(radio):
    """Función para calcular el área de un círculo según su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Salida:
    Return = float: El área del círculo.
    """
    return 3.14 * radio ** 2

def volumen_del_cilindro(radio, altura):
    """Función para calcula el volumen de un cilindro según su radio y altura.

    Parámetros:
    radio (float)   : El radio del cilindro.
    altura (float)  : La altura del cilindro.

    Salida:
    float: volumen del cilindro.
    """
    return area_del_circulo(radio) * altura

# Solución :
radio_circulo = 2
area = area_del_circulo(radio_circulo)
print("Área del círculo con radio", radio_circulo, "es:", area)

radio_cilindro = 2
alt_cilindro = 4
volumen = volumen_del_cilindro(radio_cilindro, alt_cilindro)
print("Volumen del cilindro con radio", radio_cilindro, "y altura", alt_cilindro, "es:", volumen)