"""Diseñar un algoritmo que permita ingresar por pantalla 10 números naturales. 
 Calcular el promedio de los números pares. Luego mostrar por pantalla el 
 resultado.""" 
 
pares=0
cantidad_nuemors_pares=0
for i in range(0,10,1):
    numero=int(input(f"ingrese numero {i+1}: "))
    if numero%2==0:
        cantidad_nuemors_pares+=1
        pares+=numero
promedio=pares/cantidad_nuemors_pares
print(f"la suma es {pares} y el promedio es {promedio}")        
      
