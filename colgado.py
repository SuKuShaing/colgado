import pantallas as p
import os
import random

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
    return palabras
    # print(palabras, len(palabras)) # 171 palabras


def seleccionar_palabra_del_desafio():
    lista_de_palabras = leer_archivo()
    palabra_seleccionada = random.choice(lista_de_palabras)
    return palabra_seleccionada
    # print(palabra_seleccionada, len(palabra_seleccionada))


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

        #Selección de la palabra
        palabra_oculta = seleccionar_palabra_del_desafio()
        cantidad_caracteres = len(palabra_oculta)
        # print(palabra_oculta, cantidad_caracteres)

        # while del juego:
        texto_completo = False
        while texto_completo == False:
            os.system("cls")
            print(f'{nombre_del_jugador}, Tu palabra a encontrar tiene {cantidad_caracteres} caracteres:')
            print(f'Tienes X intentos')

            # print('')
            # print(Aquí debe ir el monito que se quema)
            # print('')

            print('')
            print('_'*cantidad_caracteres) #AQUÍ SE DEBE ACTUALIZAR SEGÚN LAS LETRAS INGRESADAS 
            print('')

            # ingrese texto
            caracter_entrante = input('Ingresa una letra: ')
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


if __name__ == '__main__':
    run()


"""
Quede en:
✔ Hay que cargar la palabra
- Hacer la validación de que el carácter ingresado sea valido
- Sí el carácter es correcto que se muestre en linea que oculta la palabra
- Hacer la pantalla del juego
- Hacer la lógica para ganar o perder 
"""