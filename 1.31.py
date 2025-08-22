#Diseñar el algoritmo que permita ingresar dos valores por ejemplo NUM1 y NUM2 y 
# luego se intercambien los valores de dichas variables, es decir que el valor que 
# tenía NUM1 ahora lo contenga NUM2 y viceversa
num1=int(input("ingrese primer numero "))
num2=int(input("ingrese segundo numero "))
print(f"primero numeor es{num1}")
print(f"segundo numeor  es {num2}")
print("cambio ")
num2=num1
num1=num2
print(f"valores intercambiados {num2,num1}")