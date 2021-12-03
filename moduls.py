# 2.6
# Variables
# Elementos escenciales
abecedario = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
especiales = " 'ñ!¡¿?<>[]¨*´+-.,:;~^`|°{}!$%&/()_@0123456789"

# Importando modulos
# Importando modulo para comprobar internet
from socket import gethostbyname, create_connection, error

def comprobacion_internet():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return "Yes"
    except error:
        return "Not"

def cifrador_root(palabra, llave, opcion):
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
                    if opcion == 1:
                        letra_cifrada = abecedario[conteo + llave-1]
                    elif opcion == 2:
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
