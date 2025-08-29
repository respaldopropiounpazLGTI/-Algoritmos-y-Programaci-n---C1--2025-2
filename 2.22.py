"""Hacer un algoritmo que pida la nota de un examen (un nº real entre 0 y 10) muestre 
 por pantalla la calificación de la siguiente forma: 
 ●   Si la nota es menor que 5 la leyenda  “En suspenso” 
 ●   Si la nota se encuentra entre 5 inclusive y 7 sin incluir la leyenda 
 “Aprobado” 
 ●   Si la nota se encuentra entre 7 inclusive y 9 sin incluir la leyenda 
 “Notable” 
 ●   Si la nota se encuentra entre 9 inclusive y 10 sin incluir la leyenda 
 “Sobresaliente” 
 ●   Si la nota es un 10 la leyenda  “Matrícula de honor” 
 Terminar  el algoritmo cuando se ingresa cero como nota. En caso que no, vuelve a 
 pedir una nota   """
 
while True:
    nota=float(input( "ingrese nota "))
    if nota==0:
         break
    elif nota<5:
        print("en suspenso ")
    elif nota>=5 or nota <7:
        print("aprobado")
    elif nota>=7 or nota <9:
        print("notable")
    elif nota >=9 or nota <10:
        print("sobre saliente ")
    elif nota==10:
        print("matricula de honor ")
    else:
        print("fuera de rango ")
        
     
 
 

     