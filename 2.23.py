""" Hacer un algoritmo que permita ingresar por pantalla números naturales al finalizar 
 informar: 
 ●   ¿Cuántos están entre el 50 y 75, ambos inclusive? 
 ●   ¿Cuántos mayores de 80? 
 ●   ¿Cuántos menores de 30
  El algoritmo debe finalizar cuando se ingresa el número 0. """
treinta=0
ochenta=0
cincuenta=0  
while True:
    numero=int(input("ingrese numero "))
    if numero==0:
        break
    elif numero<30:
        treinta+=1
    elif numero>=50 and numero<=75:
        cincuenta+=1
    elif numero>80:
        ochenta+=1
        
        
        
print(f" numeros menores de 30 {treinta}")
print(f" numeros entre 50 y 75 {cincuenta}")
print(f" numeros mayores a ochenta {ochenta} ")        
        
 