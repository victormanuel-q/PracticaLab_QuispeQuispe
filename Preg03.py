# Autor: Pilar_Navarro     
cadena = input ("Cadena: ")
total_caracteres = len(cadena)-(len(cadena.split())-1)
print (f"Resultado: {total_caracteres}")