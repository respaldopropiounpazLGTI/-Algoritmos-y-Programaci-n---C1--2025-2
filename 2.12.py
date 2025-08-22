# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla 
# una a una las letras de la palabra introducida empezando por la última. 
# Ejemplo. Ingresa: Hola

palabra=input("ingrese palabra")
for i in range(len(palabra)-1,-1,-1):#esto muy raro se que empeiza asta y paso pero funciona y no se toca
    print(palabra[i])