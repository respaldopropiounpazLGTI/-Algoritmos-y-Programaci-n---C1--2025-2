 #1.4.   Ingresar dos números e informar la suma, multiplicación, división y resta de ellos. Si 
 # el segundo número es cero la división debe mostrar “No puede realizarse la 
 # operación
 
numero1=int(input("ingrese numero 1"))
numero2=int(input("ingrese numero 2"))
suma=numero1+numero2
multi=numero1*numero2
print("resultados ")
print(f"la suma es {suma}")
print(f"la multiplicacion  es {multi}")
if numero2==0:
    print("no se puede dividir por 0 ")
else:
    division =numero1/numero2
    print(f"la division es {division}")
