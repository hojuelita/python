def esPalindomo(s):

	#eliminamos los espacios en la cadena
	s1 = s.replace(' ','')

	#convertimos la cadena a minúsculas
	s1 = s1.lower()
	
	#recorremos la cadena s1 al revés y la almacenamos en s2
	s2 = s1[::-1]

	#si la cadena original y la invertida son iguales regresa True
	return s1 == s2


cadena = input("Ingresa una cadena: ")

if(esPalindomo(cadena)):
	print(cadena + ", es palíndromo")
else:
	print(cadena  + ", no es palíndromo")

