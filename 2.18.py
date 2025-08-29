"""Hacer un algoritmo que permita ingresar diez (10) números, luego muestre por 
 pantalla cuántos eran mayores a cero y cuántos son menores a cero"""
 
mayor=0
menor=0
for i in range(10):
    numero=int(input(f"ingrese numero {i+1} :"))
    if numero>0:
        mayor+=1
    elif numero<0:
        menor+=1
    elif numero==0:
        pass
        
print(f" cantidad mayor a o {mayor}")
print(f"cantidad manores a 0 {menor}")            
        