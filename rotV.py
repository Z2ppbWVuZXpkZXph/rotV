# Importando modulos
import os

#Colores
GL = "\033[96;1m" # Azul agua
BB = "\033[34;1m" # Azul claro
YY = "\033[33;1m" # Amarillo claro
GG = "\033[32;1m" # Verde claro
WW = "\033[0;1m"  # Blanco claro
RR = "\033[31;1m" # Rojo claro
CC = "\033[36;1m" # Cyan claro
B = "\033[34m"    # Azul
Y = "\033[33;1m"  # Amarillo
G = "\033[32m"    # Verde
W = "\033[0;1m"   # Blanco
R = "\033[31m"    # Rojo
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

def funcion1(x):
	try:
		llave = int(input(BB+"Pon tu llave\n>>> "+WW))
	except ValueError as e_V:
		print (RR+"ERROR:"+WW+" Procura usar números a la proxima vez"+RR+"\nError intérprete:"+WW, e_V)
		exit(1)
	except KeyboardInterrupt as e_K:
		print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
		exit(1)

	try:
		palabra = input(BB+"Pon el dato que quieras cifrar\n>>> "+WW)
	except KeyboardInterrupt as e_K:
		print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
		exit(1)

	if palabra == "":
		print (GG+"\nEl resultado es\n>>> ", end="" +WW+ "No ingresaste nada\n")
		exit(1)

	# Imprimiendo el resultado
	print (GG+"\nEl resultado es\n>>> ", end="" +WW)

	# Calculando algoritmo
	conteo = 1
	for letras1 in palabra:
		for caracteres in especiales:
			if letras1 == caracteres:
				print (caracteres, end="")
				break
			elif letras1 == "á":
				letras1 = "a"
			elif letras1 == "é":
				letras1 = "e"
			elif letras1 == "í":
				letras1 = "i"
			elif letras1 == "ó":
				letras1 = "ó"
			elif letras1 == "ú":
				letras1 = "u"
			else:
				pass
		else:
			letras = str.lower(letras1)
			for letras_a in abecedario:	
				if letras == letras_a:
					letra_detectada = abecedario[conteo -1]
					letra_detectada = abecedario[conteo -1]
					if x == 1:
						letra_cifrada = abecedario[conteo + llave-1]
					elif x == 2:
						letra_cifrada = abecedario[conteo - llave-1]
					if letras1 == str.upper(letras):
						letra_cifrada = str.upper(letra_cifrada)
						print (letra_cifrada, end="")
					else:
						print (letra_cifrada, end="")
					conteo = 1
					break
				else:
					conteo = conteo + 1
	print ("")

# Inicializacion
os.system("clear")

# Elementos escenciales
abecedario = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
especiales = " 'ñ!¡¿?<>[]¨*´+-.,:;~^`|°{}!$%&/()_@0123456789"

# Titulo
print (GG+"""              _ __     __
    _ __ ___ | |\ \   / /
   | '__/ _ \| __\ \ / /
   | | | (_) | |_ \ V /
   |_|  \___/ \__| \_/     Versión 2.0
""")
print (WW+"¡Bienvenido a mi nueva herramienta de rot y cifrados!")
print (WW+"A diferencia de otras herramientas, esta", RR+ "identifica espacios y caracteres especiales!")

print (YY+"Para comenzar, ¿Qué es lo que quieres hacer?")
print (RR+"   1)"+WW+" Cifrar\n  "+RR+" 2) "+WW+"Descifrar\n  "+RR+" 3) "+WW+"Salir\n")

try:
	funcion = int(input(BB+"Elige una opcion: "+WW))
except ValueError as e_V:
	print (RR+"ERROR:"+WW+" Procura usar números a la proxima vez"+RR+"\nError intérprete:"+WW, e_V)
	exit(1)
except KeyboardInterrupt as e_K:
	print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
	exit(1)

if funcion == 1:
	print (GG+"      ¡Es la hora de cifrar!")
	funcion1(1)
elif funcion == 2:
	print (GG+"         ¡Es la hora de descifrar!")
	funcion1(2)
elif funcion == 3:
	print (RR+"Saliendo del programa...")
	exit(1)

