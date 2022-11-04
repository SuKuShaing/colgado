import pantallas as p
import os

def verificar_texto(texto):
    if len(texto) > 0:
        # print(texto, len(texto), type(len(texto)))
        return True
    else:
        print("Ingrese un nombre")
        return False


def texto_salir(texto):
    if texto == p.mensaje_salir:
        os.system("cls")
        print(p.mensaja_de_adios)


def leer_archivo():
    palabras = []
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append(line[:-1])
    # print(palabras, len(palabras)) # 171 palabras


def run():
    #Bienvenida al juego
    os.system ("cls")
    print(p.mensaja_de_bienvenida)

    #Deseas jugar?
    jugar = input("¿Deseas jugar? (Escriba 'Y' para SI y 'N' para NO): ")

    if jugar in p.respuesta_positiva:
        os.system("cls")
        
        #Ingrese su nombre
        nombre_valido = False
        while nombre_valido == False:
            nombre_del_jugador = input("Escribe tu nombre: ")
            nombre_valido = verificar_texto(nombre_del_jugador)
        print(f'"{nombre_del_jugador}" es un nombre valido')

        # while True:
        texto_completo = False
        while texto_completo == False:
            pass
            leer_archivo()
            break
            # ingrese texto
            # Sí palabra completa es igual a la solicitada
                #pantalla GANASTE
            # si, limite de intentos superado
                #Pantalla Perdiste

    # os.system("cls")
    # print(p.mensaja_de_adios)

    

    #Cargar palabra de la lista de facundo
    #Input de letras
    #Verificar que sea un carácter valido
    #Contar intentos
    #pantalla de Ganaste o Perdiste
    pass

if __name__ == '__main__':
    run()
    # leer_archivo()



"""
Quede en:
- Hay que cargar la palabra, 
- que la persona
- hacer la lógica para ganar o perder 
"""