import pantallas as p
import os
import random

def verificar_longitud_texto(texto):
    if len(texto) > 0:
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


def seleccionar_palabra_del_desafio():
    lista_de_palabras = leer_archivo()
    palabra_seleccionada = random.choice(lista_de_palabras)
    return palabra_seleccionada
    # return 'pingüino' #pruebas para el acento


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
            nombre_valido = verificar_longitud_texto(nombre_del_jugador)
        print(f'"{nombre_del_jugador}" es un nombre valido')

        #Selección de la palabra
        palabra_oculta = seleccionar_palabra_del_desafio()
        cantidad_caracteres = len(palabra_oculta)
        respuesta_jugador = []
        for i in range(cantidad_caracteres):
            respuesta_jugador.append('_')

        # while del juego:
        texto_completo = False
        while texto_completo == False:
            os.system("cls")
            print(f'{nombre_del_jugador}, Tu palabra a encontrar tiene {cantidad_caracteres} caracteres:')
            print(f'Tienes X intentos')

            # print('')
            # print(Aquí debe ir el monito que se quema)
            # print('')

            #Linea punteada donde se muestra la respuesta del usuario
            print('')
            mostrar_respuesta_jugador = "".join(respuesta_jugador)
            print(mostrar_respuesta_jugador)
            print('')

            # ingrese texto
            caracter_entrante = input('Ingresa una letra: ')

            # Validación de la palabra, sí es correcta se coloca en el array de respuesta del jugador
            indice = 0
            for letra_oculta in palabra_oculta:
                
                # Solo entraría aquí si la letra a testear tiene acento o diéresis
                acento = -1
                if letra_oculta in p.caracteres_acentuados:
                    print(p.caracteres_acentuados.index(letra_oculta))
                    acento = p.caracteres_acentuados.index(letra_oculta)
                    letra_oculta = p.caracteres_no_acentuados[p.caracteres_acentuados.index(letra_oculta)]
                    print('acento: ', acento)

                # Verifica que la letra ingresada coincida con alguna del array oculto
                if caracter_entrante == letra_oculta:
                    if acento != -1:
                        # Sí la letra oculta tiene acento, aquí se le devuelve el acento para que aparezca en la pantalla correctamente escrita
                        respuesta_jugador[indice] = p.caracteres_acentuados[acento]
                    else:
                        respuesta_jugador[indice] = letra_oculta

                indice += 1


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
✔ Hacer la validación de que el carácter ingresado sea valido - no es necesario, puesto que el usuario debe velar por ingresar caracteres validos
✔ Sí el carácter es correcto que se muestre en linea que oculta la palabra
✔ Verificar que solo ingrese un carácter por vez - ¿por qué? debería dejarme introducir varias palabras a la vez
✔ Colocar la lógica de la validación de la letra aunque tenga acento del acento
- Hacer la lógica para ganar 
- Hacer la lógica para perder 
"""