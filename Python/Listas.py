'''
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares.
Para ordenar una lista automáticamente puedes utilizar el método .sort().
numeros = [-12, 84, 13, 20, -33, 101, 9]
'''
numeros = list(map(int, input("Ingresa los numeros de la lista: ").split()))


def separar(lista):
    lista.sort()  # Acomodo de la lista
    pares = []  # Definir listas vacias
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)

        else:
            impares.append(i)

    return pares, impares


par, impar = separar(numeros)
print(par)
print(impar)
