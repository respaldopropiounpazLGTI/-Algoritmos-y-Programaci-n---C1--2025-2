#Escribir un programa en el que se pregunte al usuario por una frase y una letra, # y 
 # muestre por pantalla el número de veces que aparece la letra en la frase
franse=input("ingrese frase").lower()
letra=input("ingrese letra a buscar ").lower()
cantidad=franse.count(letra)

print(letra,cantidad)
