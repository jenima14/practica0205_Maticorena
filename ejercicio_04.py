def calcular_media(lista):
    """Función que calcula la media de una lista de números.

    Parametros:
    lista (list): Lista de números para calcular la media.

    Salida:
    float: La media de los números en la lista.
    """
    if not lista:
        return 0
    
    suma = sum(lista)
    media = suma / len(lista)
    return media

# Solución de uso:
numeros = [5, 10, 15, 20, 25]
resultado_media = calcular_media(numeros)
print("La media de la muestra es:", resultado_media)