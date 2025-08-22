 #Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 
 # veces. (realizarlo con while y con for)
nombre=input("ingrese nombre")
vueltas=10
for i in range(vueltas):
    print(f"{nombre} {i+1}" )
    
apellido=input("ingrese apellido ")
contador=0
while True:
    print(apellido)
    contador+=1
    if contador==10:
        break