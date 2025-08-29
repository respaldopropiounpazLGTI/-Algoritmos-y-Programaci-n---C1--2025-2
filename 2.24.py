"""Hacer un algoritmo que permita convertir calificaciones numéricas a letras, según 
 la siguiente tabla: 
 ●   A=10 
 ●   B= 8 y 9
  ●   C=6 y 7 
 ●   D=4, y 5 
 ●   E=1 hasta el 4. 
 Se asume que la nota está comprendida entre 1 y 10.  (En caso de ingresar números fuera 
 de rango, informar con un mensaje “Rango nota invalido” 
 Informar por pantalla la calificación (Letra) que se sacó. 
 El programa finaliza cuando se ingresa el número cero o menor"""
while True:
    nota=int(input("ingrese nota"))
    if nota==0:
        break
    elif nota ==10:
        print("A")
    elif nota==8 or nota==9:
        print("B")
    elif nota==6 or nota==7 :
        print("C")
    elif nota >=4 or nota==5:
        print("D")
    elif nota==1 or nota<=4:
        print("E")
    else:
        print("fuera de valor ")
