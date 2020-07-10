#Autor Quispe Quispe Victor Manuel
numero_ingresado = (input("Numero: "))
revertir = 0
try:
    valor = int(numero_ingresado)
    while valor > 0:
        residuo = valor % 10
        revertir = (revertir * 10) + residuo
        valor //= 10
    print('Resultado: ', revertir)
except ValueError:
    print("Ese numero no es valido.!")