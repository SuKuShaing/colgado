import pantallas as p
import os

def run():
    #Bienvenida al juego
    os.system ("cls")
    print(p.mensaja_de_bienvenida)

    #Deseas jugar?
    jugar = input("¿Deseas jugar? (Escriba 'Y' para SI y 'N' para NO): ")

    if jugar in p.respuesta_positiva:
        os.system ("cls")
        print("gracias por jugar")
    else:
        os.system ("cls")
        print(p.mensaja_de_adios)

    #Ingrese su nombre
    # nombre_del_jugador = input("Escribe tu nombre: ")
    

    #Cargar palabra de la lista de facundo
    #Input
    #Verificar que sea un carácter valido
    #Contar intentos
    #pantalla de Ganaste o Perdiste
    pass

if __name__ == '__main__':
    run()


# print(list(enumerate(p.respuesta_positiva))) #[(0, 'yes'), (1, 'YES'), (2, 'y'), (3, 'Y'), (4, 'si'), (5, 'SI'), (6, 'sí'), (7, 'SÍ'), (8, 's'), (9, 'S')]