""" Hacer un algoritmo que permita ingresar por pantalla cinco (5) números y luego 
 calcular su media."""
sumando=0
for i in range(5):
    numero=int(input(f"ingrese numero {i+1}"))
    sumando+=numero
promedio=sumando/5
print(f"la suma es {sumando} y la media es {promedio}")    