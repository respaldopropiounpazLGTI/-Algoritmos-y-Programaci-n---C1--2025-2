#Escribir un programa que pregunte el nombre del usuario en la consola y un número 
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido
nomvre=input("ingrese nombre ")
numero=int(input("ingrese numero "))
for nombre  in range(numero):
    print(f"{nomvre} {nombre+1}")