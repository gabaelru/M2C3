# Ejercicio 1 - Creacion de variables
cadena = "Estoy programando en Python hoy"
numero = 2021
lista = [1,2,3,4,5,6,7,8,9,10]
booleano = True


# Ejercicio 2 - Use an index to grab the first 3 letters in your string
cadena_corta = cadena[0:3]
print(cadena_corta)

# Ejercicio 3 - Use an index to grab the first element from your list
primer_elemento = lista[0]
print(primer_elemento)

# Ejercicio 4 - Create a new number variable that adds 10 to your original number
numero_add = numero + 10
print(numero_add)

# Ejercicio 5 - Use an index to get the last element in your list
ultimo_elemento = lista[-1]
print(ultimo_elemento)

# Ejercicio 6 - Use split to transform the following string into a list
names = 'harry,alex,susie,jared,gail,conner'
lista_names = names.split(',')
print(lista_names)

"""
Ejercicio 7 - Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
"""
lista_cadena = cadena.split(' ')
palabra_mayuscula = lista_cadena[0].upper()
nueva_cadena = cadena.replace(lista_cadena[0], palabra_mayuscula)
print(nueva_cadena)

# Ejercicio 8 - Use string interpolation to print out a sentence that contains your number variable
print(f'El número elegido es: {numero}')

# Ejercicio 9 - Print “hello world”
print("hello world")
