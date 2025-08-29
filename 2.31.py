"""Desarrollar un programa que permita ingresar números  mayores que 0 (cero), 
 finalizar el ingreso cuando no se cumpla esta condición e informar el valor menor y 
 el valor mayor del conjunto"""
mayor=0
menor=0
while True:
    numero=int(input("ingrese numeor "))
    if numero<0:
        break
    elif numero>mayor:
        mayor=numero
    else:
        menor=numero
        
print(f"numero mayor{mayor}")
print(f"numero menor{menor}")        
     