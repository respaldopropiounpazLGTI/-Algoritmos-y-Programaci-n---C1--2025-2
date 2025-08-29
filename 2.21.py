"""Hacer un algoritmo que se ingresan 20 números enteros, calcular cuántos números 
impares y cuántos números pares fueron ingresados"""
inpares=0
pares=0
for i in range(20):
    numero=int(input(f"ingrese numero {i+1} : "))
    if numero %2==0:
        pares+=1
    elif numero%2!=0:
        inpares+=1
        
print(f"cantidad de numero inapres {inpares}")
print(f"cantidad de numero pares {pares}")         