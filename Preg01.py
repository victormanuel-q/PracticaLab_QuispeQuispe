#AUTOR: LUIS IZQUIERDO

def pregunta1(numero):
    cont = 0
    for n in range(1, numero+1):
        if numero % n == 0:
            cont += 1

    if cont == 2:
        print("El numero ingresado si es primo")
    else:
        print("El numero ingresado no es primo")
        
numero = int(input("Dato de entrada: "))
print()
pregunta1(numero)