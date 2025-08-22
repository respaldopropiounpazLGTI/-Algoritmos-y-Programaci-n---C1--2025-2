#Escribir un programa que pida al usuario un número entero positivo y muestre por 
# pantalla todos los números impares desde 1 hasta ese número separados por coma
numero_fijo=0
numero=int(input("ingrese numero "))
if numero<0:
    print("solo numero positivos ")

elif numero>0 and numero %3==0:
    numero_fijo=numero
    print(numero_fijo)  
    
#no se como hacer la logica del inpar asta ese numero 