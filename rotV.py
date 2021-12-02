# 2.1
# Importando modulos
import os, moduls, subprocess, sys, time

# Comprobando si hay internet disponible para comprobar actualizacion
conexion = moduls.comprobacion_internet()

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

# Definiendo carga
listo = False
def animacion():
    while listo == False:
        sys.stdout.write("\rActualizando herramienta |")
        time.sleep(0.1)
        sys.stdout.write("\rActualizando herramienta /")
        time.sleep(0.1)
        sys.stdout.write("\rActualizando herramienta -")
        time.sleep(0.1)
        sys.stdout.write("\rActualizando herramienta \\")
        time.sleep(0.1)
    sys.stdout.write("\rActualizacion terminada!")

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)
                
# Definiendo interfaz
documento = open("moduls.py", "r")
lineas = documento.readlines()[0]
version = lineas[2:-1]
version = str(version)

titulo_1 = (GG+"""              _ __     __
    _ __ ___ | |\ \   / /
   | '__/ _ \| __\ \ / /
   | | | (_) | |_ \ V /
   |_|  \___/ \__| \_/     Versión {}
""".format(version))

def interfaz(x):
	if x == 1:
		print (titulo_1)
		print (WW+"¡Bienvenido a esta nueva herramienta de rot y cifrados!")
		print (WW+"A diferencia de otras herramientas, esta", RR+ "identifica espacios y caracteres especiales!")
		print (YY+"Para comenzar, ¿Qué es lo que quieres hacer?")
		print (RR+"   1)"+WW+" Cifrar\n  "+RR+" 2) "+WW+"Descifrar\n  "+RR+" 3) "+WW+"Salir\n")
	elif x == 2:
		os.system("clear")
		print (titulo_1)
		print (WW+"¡Hola, vengo a decirte que hay una nueva version de este programa disponible!")
		print (Y+"¿Deseas actualizarlo a la version {}?".format(version1))
		print (RR+"   1)"+WW+" Si\n  "+RR+" 2) "+WW+"No\n")
		opcion_update = int(input(BB+"Selecciona una opcion: "+ WW))
		if opcion_update == 1:
			sutil(GG+"\n Actualizando Herramienta...")
			# Eliminando directorio desactualizado
			comando_eliminar = "rm -rf rotV"
			comando_instalar = "git clone https://github.com/Z2ppbWVuZXpkZXph/rotV"
			sutil(RR+"["+WW+"+"+RR+"]"+YY+" Cargando variables")
			os.chdir("..")
			sutil(RR+"["+WW+"+"+RR+"]"+YY+" Se Actualizó la herramienta correctamente")
			sutil(GG+" Disfrutalo!")
			os.system(comando_eliminar)
			subprocess.run(comando_instalar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			os.chdir("rotV")
			os.system("python3 rotV.py")
		else:
			pass


def oportunidad_actualizar():
 	interfaz(2)
          
# Comprobando si es posible revisar la actualizacion o no
if conexion == "Yes":
    # Importando variables
    global a
    # Identificando version del programa actual
    documento = open("moduls.py", "r")
    lineas = documento.readlines()[0]
    version = lineas[2:-1]
    version = str(version)
 
	# Identificando version del programa en linea
    comando = "wget https://raw.githubusercontent.com/Z2ppbWVuZXpkZXph/rotV/main/rotV.py"
    subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    documento1 = open("rotV.py.1", "r")
    lineas1 = documento1.readlines()[0]
    version1 = lineas1[2:-1]
    os.system("rm rotV.py.1 &")

	# Comparando versiones de diferentes documentos
    if version != version1:
    	oportunidad_actualizar()
    else:
    	a = "b2"
else:
    pass

def cifrar(x):
	if x == 1:
		os.system("clear")
		print (titulo_1)
		print (Y+" Es momento de cifrar oraciones a continuación:\n")
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
		# Calculando oracion
		moduls.cifrador_root(palabra, llave, 1)
	
		print ("")

def descifrar(x):
	if x == 1:
		os.system("clear")
		print (titulo_1)
		print (Y+" Es momento de descifrar oraciones a continuación:\n")
		try:
			llave = int(input(BB+"Pon tu llave\n>>> "+WW))
		except ValueError as e_V:
			print (RR+"ERROR:"+WW+" Procura usar números a la proxima vez"+RR+"\nError intérprete:"+WW, e_V)
			exit(1)
		except KeyboardInterrupt as e_K:
			print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
			exit(1)

		try:
			palabra = input(BB+"Pon el dato que quieras descifrar\n>>> "+WW)
		except KeyboardInterrupt as e_K:
			print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
			exit(1)

		if palabra == "":
			print (GG+"\nEl resultado es\n>>> ", end="" +WW+ "No ingresaste nada\n")
			exit(1)

		# Imprimiendo el resultado
		print (GG+"\nEl resultado es\n>>> ", end="" +WW)
		# Calculando oracion
		moduls.cifrador_root(palabra, llave, 2)	
		print ("")

# Inicializacion
os.system("clear")

# Titulo
interfaz(1)
try:
	funcion = int(input(BB+"Elige una opcion: "+WW))
except ValueError as e_V:
	print (RR+"ERROR:"+WW+" Procura usar números a la proxima vez"+RR+"\nError intérprete:"+WW, e_V)
	exit(1)
except KeyboardInterrupt as e_K:
	print (RR+"\nSaliendo:"+WW+" Estas a punto de salir del programa"+RR+"\nIntérprete:"+WW, "KeyboardInterrupt")
	exit(1)

if funcion == 1:
	cifrar(1)
elif funcion == 2:
	descifrar(1)
elif funcion == 3:
	exit(1)

