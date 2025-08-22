 #Escribir un programa que pida al usuario un número entero y muestre por pantalla 
 # un triángulo rectángulo. 
 #EJ: para 5 
 #* 
 #** 
 #*** 
 #*** 
 #****
 
numero=int(input("ingrese numero "))
for i in range(numero+1):
    print(i*("*"))