def valor_cuadrado(lista_num):
    """Funcion que calcula los valores al cuadrado de una lista de números.

    Paramétros:
    lista_num (list): Lista de números para elevar al cuadrado.

    Salida:
    list: Lista con los valores al cuadrado de la muestra de números.
    """
    muestra_num = [num ** 2 for num in lista_num]
    return muestra_num

# solución de uso:
numeros = [2, 4, 6, 8, 10]
resultado_cuadrado = valor_cuadrado(numeros)
print("Valores al cuadrado de la muestra:", resultado_cuadrado)