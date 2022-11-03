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
"""