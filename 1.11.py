#Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
hora=int(input("ingrese cantidad de horas trabajadas "))
coste=int(input(" ingrese coste por hora "))
sueldo=hora*coste
print(f"como trabajo {hora} y el coste es {coste} el sueldo bruto sera de {sueldo}")