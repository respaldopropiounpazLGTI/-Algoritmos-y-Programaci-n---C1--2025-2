#Hacer un algoritmo que permita ingresar tres números enteros y, si el primero de 
# ellos es negativo, calcular el producto de los tres, en caso contrario calcular la suma de ello
numero1=int(input("ingrese primer  numero "))
numero2=int(input("ingrese segundo numero "))
numero3=int(input("ingrese tercer  valor "))
if numero1<0:
    prodcuto=numero1*numero2*numero3
    print(f" el producto de los 3 numeros es {prodcuto}")
else:
    suma=numero1+numero2+numero3
    print(f"la suma es {suma} ")