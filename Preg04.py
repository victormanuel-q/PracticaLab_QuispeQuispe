#Autor Quispe Quispe Victor Manuel


def integrantes():
    archivo = open("noticia.txt","at")
    contenido = "\nCABALLERO MORENO, ISABELLA \nIZQUIERDO ROJAS, LUIS ANGEL \nNAVARRO ESPINOZA, PILAR \nQUISPE QUISPE, VICTOR"
    archivo.write(contenido)
    archivo.close()

integrantes()

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