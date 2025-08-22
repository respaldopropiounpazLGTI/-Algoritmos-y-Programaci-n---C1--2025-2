# Hacer un algoritmo que se ingresa tres números. Mostrar por pantalla si están 
# ordenados de menor a mayor

numero1=int(input("ingrese valor 1 "))
numero2=int(input("ingrese valor 2 "))
numero3=int(input("ingrese valor 3 "))
if numero1<numero2 and numero1<numero3:
    print(f"valor 1 {numero1} es menor a todos {numero2 } y {numero3}")
elif numero2<numero3:
    print(f" valor 2 es manor a {numero3}")
else:
    print(f"valor 3 {numero3} es manor ")