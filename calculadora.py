import sys

# Leemos los argumentos pasados por el usuario
# el primero corresponde al tipo de operación
# el segundo y tercero son los números a operar
op = str(sys.argv[1])
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])

# Operamos de acuerdo a la operación que ingresó el
# usuario e imprimimos el resultado, en caso que la
# operación no esté definida en nuestro programa le
# pedimos que ingrese una operación válida
if(op=="suma"):
	print("Resultado: "+ str(n1+n2))
elif(op=="resta"):
	print("Resultado: "+ str(n1-n2))
elif(op=="producto"):
	print("Resultado: "+ str(n1*n2))
elif(op=="division"):
	print("Resultado: "+ str(n1/n2))
else:
	print("Ingrese una operación válida: [ suma | resta | producto | division ]")
