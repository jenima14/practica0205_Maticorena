def decimal_binario(num_decimal):
    """Función que convierte un número decimal en binario.

    Parámetro:
    numero_decimal (int): Número decimal a convertir.

    Salida:
    Return = str: Representación en binario del número decimal.
    """
    binario = bin(num_decimal)[2:]
    return binario

def binario_decimal(num_binario):
    """Función que convierte un número binario en decimal.

    Parámetro:
    numero_binario (str): Número binario a convertir.

    Salida:
    Return = int: Representación decimal del número binario.
    """
    decimal = int(num_binario, 2)
    return decimal

# Solución para convertir decimal a binario
decimal = 16
sol_binario = decimal_binario(decimal)
print("El número", decimal, "en binario es:", sol_binario)

# Solución para convertir binario a decimal
binario = '11111'
sol_decimal = binario_decimal(binario)
print("El número binario", binario, "en decimal es:", sol_decimal)