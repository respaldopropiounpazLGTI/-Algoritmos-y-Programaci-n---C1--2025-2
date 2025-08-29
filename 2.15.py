 #Hacer un algoritmo que se ingrese 10 letras. Mostrar cuál es la mayor letra  ingresada
mayor=""
for i in range(10):
    letra=input(f"ingrese letra {i+1} : ")
    if letra>mayor:
        mayor=letra
        
        
        
        
print(f"la letra mayor es {mayor}")        