#Ingresar dos números y mostrar el menor de ellos. El ejercicio finaliza cuando se 
# ingresan números iguales

while True:
    numero1=int(input(f"ingrese primer numero "))
    numero2=int(input(f"ingrese segundo numero "))
    if numero1==numero2:
        print(f"numero iguale {numero1}=={numero2} ")
        break 