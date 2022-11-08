mensaja_de_bienvenida = """
██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ 
██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗
██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║
██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║
██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝
╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ 

En este juego deberás encontrar las letras de la palabra misteriosa para 
salvar tu alma y la vida del personaje
"""

mensaja_de_adios = """
_█████╗ ██████╗ ██╗ ██████╗ ███████╗        ██████╗ ██████╗ 
██╔══██╗██╔══██╗██║██╔═══██╗██╔════╝        ██╔══██╗██╔══██╗
███████║██║  ██║██║██║   ██║███████╗        ██████╔╝██████╔╝
██╔══██║██║  ██║██║██║   ██║╚════██║        ██╔══██╗██╔══██╗
██║  ██║██████╔╝██║╚██████╔╝███████║        ██████╔╝██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚══════╝        ╚═════╝ ╚═════╝ 
"""

respuesta_positiva = ['yes', 'YES', 'y', 'Y' , 'si', 'SI', 'sí', 'SÍ', 's', 'S']
mensaje_salir = ['Salir', 'SALIR', 'salir', 'Exit', 'EXIT', 'exit']
caracteres_acentuados =['á', 'é', 'í', 'ó', 'ú', 'ü']
caracteres_no_acentuados =['a', 'e', 'i', 'o', 'u', 'u']



# pagina para generar las letras https://fsymbols.com/es/generadores/tarty/
# Mejor usar esta https://patorjk.com/software/taag/ la de arriba no funciona en las terminales Bash

persona_congada = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



def sacar_acentos(s): # Remueve los acentos de una frase
    "Enviar un string para que los reemplace"
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
      print( a , b)

      s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



"""
dic = {"A":1, "b":2}
print(dic.get("A")) #1
print(dic.get("a")) #None | Falla, hay que acceder al diccionario con el texto tal cual
print(dic.get("b")) #2
print(type(dic.get("C"))) #None | <class 'NoneType'>

os.system ("clear") #Unix 
os.system ("cls") #Windows

# print(list(enumerate(p.respuesta_positiva))) #[(0, 'yes'), (1, 'YES'), (2, 'y'), (3, 'Y'), (4, 'si'), (5, 'SI'), (6, 'sí'), (7, 'SÍ'), (8, 's'), (9, 'S')]

Strings are immutable in Python!!!!!!!!!!!!!!!!!!!!!!!!
"""