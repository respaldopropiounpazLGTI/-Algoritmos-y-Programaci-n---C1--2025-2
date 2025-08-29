"""Hacer un algoritmo que se ingresan 50 números enteros, calcular cuántos números 
impares se ingresaron"""

inpares=0
for i in range(0,50,1):
    numero=int(input(f"ingrese numero {i+1} : "))
    if numero%2!=0:
        inpares+=1
        
print(f" se ingresaron {inpares } inpares ")        
        
    
     