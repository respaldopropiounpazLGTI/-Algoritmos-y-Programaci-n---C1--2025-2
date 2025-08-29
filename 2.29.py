"""Desarrollar un algoritmo que lea una lista de 20 números y determine cuántos son 
 positivos, y cuantos son negativos"""
positivos =0
negativos=0
for i in range(0,20,1):
    numero=int(input(f"ingrese numero {i+1} : "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
        
        
        
print(f"cantidad numeros positivos {positivos}")
print(f"cantidad numero negativos {negativos}")        