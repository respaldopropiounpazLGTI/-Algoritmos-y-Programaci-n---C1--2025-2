#Hacer un algoritmo que nos permita introducir un número, luego muestre por 
# pantalla el mensaje “Este número es par” o “este número es impar
numero=int(input("ingrese numero "))
if numero%2==0:
    print(f"{numero} este numero es par")
else:
    print(f"{numero} este numero es inpar")