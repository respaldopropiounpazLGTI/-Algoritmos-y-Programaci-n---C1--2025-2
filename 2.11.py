#Hacer un algoritmo donde se ingresan 10 números enteros. Mostrar por pantalla el 
 #número más grande ingresado y en qué posición se ingres
cantidad=2
mayor=0
menor=99
for i in range(cantidad):
    numero=int(input(f"ingrese numermo {i+1} :"))
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero
        
print(f"numero mas grande {mayor} y numero mas chico {menor}")        
         