#Hacer un algoritmo que se ingresan 10 números enteros, mostrar por pantalla la 
# cantidad de números pares que se ingresaron.
cantidad=10
pares=0
inpares=0
for i in range(cantidad):
    numero =int(input(f"ingrese numero {i+1} "))
    if numero%2==0:
        pares+=1
    else:
        inpares+=1
        
print(f"cantidad de pares {pares} y cantidad de inpares {inpares}")        