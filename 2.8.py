#Escribir la tabla de multiplicar de un número el cual se pide por pantalla.  Ej. Calcule la tabla del: 5 

numero=int(input("ingrese numero "))
for i in range(11):
    print(numero,"x",i,numero*i)