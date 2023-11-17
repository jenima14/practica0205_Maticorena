#Solución bucles iterativos
def bucle(numero_entero1):
    """Función que calcula el factorial de un número.

    Parámetros:
    numero (int): Número entero positivo del cual se calculará el factorial.

    Salida:
    Returns = int: resultado del cálculo del factorial.
    """
    solucion1 = 1
    for i in range(1, numero_entero1 + 1):
        solucion1 *= i
    return solucion1

num1 = 3
sol_iterativo = bucle(num1)
print("El factorial de", num1, "es:", sol_iterativo)

#Solución función recursiva
def recursivo(numero_entero2):
    """Función que calcula el factorial de un número

    Parámetros:
    numero (int): Número entero positivo del cual se calculará el factorial.

    Salida:
    Returns = int: resultado del cálculo del factorial.
    """
    if numero_entero2 == 0 or numero_entero2 == 1:
        return 1
    else:
        return numero_entero2 * recursivo(numero_entero2 - 1)

num2 = 4
sol_recursivo = recursivo(num2)
print("El factorial de", num2, "es:", sol_recursivo)