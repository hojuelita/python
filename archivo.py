#Escribimos el texto que ingrese el usuario en el documento archivo.txt
file = open('archivo.txt','w')
cad = input('Ingrese una cadena: ')
file.write(cad)

#Ahora leemos el contenido del archivo
print("Leyendo el documento... ")
file = open('archivo.txt','r')
print(file.read())

#Finalmente, eliminamos los datos guardados en el archivo
print("Los datos se borrarán automáticamente.")
file = open('archivo.txt','w+')
file.write('')

file.close()