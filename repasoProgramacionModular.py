#crear una funcion con parametros indeterminados y que escriba los numeros pares e impares
"""
def cuenta_atras(num):
    num= num - 1
    if num > 0:
        cuenta_atras(num)
    else:
        print("fin")


cuenta_atras(10)


def funcion_par_impar(*n):
    if n % 2 == 0:
        return print("Es par ")
    else:
        return print("No es par ")

funcion_par_impar((5))
"""





def funcion_par_impar (argumentos):
    pares=[]
    impares=[]

    for valor in argumentos:
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)


    return (pares,impares)
#print("La lista de {} es {} y {}".format((argumentos,pares, impares)))



print(funcion_par_impar([1,2,6,48,78,65]))



