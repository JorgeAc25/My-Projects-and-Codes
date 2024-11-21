"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example a = [1, 1, 2, 2, 4, 4, 5, 5, 5]



There are two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.
"""

def pickingNumbers(a):
    arr_temp = []
    arr_final = []
    a.sort()
    print(a)

    for i in range(1, len(a)):
        print("valor de a[i]:", a[i], "valor de a[i-1]:", a[i-1])

        # Evaluar si arr_temp esta vacio y agregar los primeros elementos consecutivos
        if (arr_temp == [] and abs(a[i] - a[i-1]) <= 1):
            arr_temp.append(a[i-1])
            arr_temp.append(a[i])
            print(f"se agregaron {a[i-1]} y {a[i]} a arr_temp")
            print(arr_temp)

        # Evaluar si el siguiente elemento sigue siendo consecutivo
        elif arr_temp and abs(a[i] - min(arr_temp)) <= 1:
            arr_temp.append(a[i])
            print(f"se agrego {a[i]} a arr_temp")
            print(arr_temp)

        else:
            # Evaluar si arr_temp es mas largo que arr_final
            if len(arr_temp) > len(arr_final):
                arr_final = arr_temp.copy()
                print(f"arr_final actualizado: {arr_final}")

            # Reiniciar arr_temp y continuar buscando
            if arr_temp:
                min_val = min(arr_temp)
                arr_temp = [x for x in arr_temp if x != min_val]
                arr_temp.insert(0,a[i])
                print(f"reiniciando arr_temp: {arr_temp}")

    # Evaluar si el ultimo arr_temp es el mas largo
    if len(arr_temp) > len(arr_final):
        arr_final = arr_temp.copy()

    return len(arr_final)

n = int(input())
a = list(map(int, input().split()))

print("El subarray mas largo es:", pickingNumbers(a))