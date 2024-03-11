def array_sum(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return (suma)

numeros = [2,4,6,8,10]
print("La suma de todos los valores de la lista es:", array_sum(numeros))