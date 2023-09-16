"""
    GDSA - Lab1 - Rafael Echevarria
"""

def parell_senar ():
    """
    Escriu una funció en el que l'usuari va introduint números i es va dient si el número és parell o senar. El programa acaba quan s'introdueix un zero.
    """
    while True:
            numero = int(input("Introdueix un número: "))
            if numero == 0:
                print("S'acaba el programa")
                break
            elif numero % 2 == 0:
                print(f"{numero} es parell.")
            else:
                print(f"{numero} es senar.")
                
def num_mayor ():
    """
    Escriu una funció que demani a l'usuari una llista de números i que torni el número més gran d'aquesta.
    """
    llista = []
    while True:
        entrada = input("Introdueix un número (o 'fi' per acabar): ")
        if entrada.lower() == 'fi':
            break
        try:
            numero = float(entrada)
            llista.append(numero)
        except ValueError:
            print("Entrada no vàlida.")
        if llista:
            max_num = max(llista)
            print(f"El numero mes gran es: {max_num}")
            
def list_comu (llista1, llista2):
    """
    Escriu una funció que donades dues llistes imprimeixi els elements que tinguin en comú.
    
    """
    comuns1 = set(llista1)
    comuns2 = set(llista2)
    
    comuns = comuns1.intersection(comuns2)
    
    if comuns:
        print("Els elements en comú són:")
        for numero in comuns:
            print(numero)

def esPrimo(numero):
    """
    La funcion devuelve `True` si su argumento es primo, y `False` si no lo es.
    
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, int(numero**0.5)+1):
        if numero % prueba == 0:
            return False
    return True

def distancia (punt1, punt2):
    # Teorema de Pitàgores per calcular la distància
    return ((punt1[0] - punt2[0]) ** 2 + (punt1[1] - punt2[1]) ** 2) ** 0.5

def T_triangle ():
    """
    Escriu una funció que demani a l'usuari 3 punts per formar un triangle i retorni el tipus de triangle format.
    """
    punt1 = (float(input("Introdueix la coordenada x del punt 1: ")), float(input("Introdueix la coordenada y del punt 1: ")))
    punt2 = (float(input("Introdueix la coordenada x del punt 2: ")), float(input("Introdueix la coordenada y del punt 2: ")))
    punt3 = (float(input("Introdueix la coordenada x del punt 3: ")), float(input("Introdueix la coordenada y del punt 3: ")))
    # Calculem les distàncies
    dist1 = distancia(punt1, punt2)
    dist2 = distancia(punt2, punt3)
    dist3 = distancia(punt3, punt1)
    # Comprovem el tipus
    if dist1 == dist2 == dist3:
        return "Triangle equilater"
    elif dist1 == dist2 or dist2 == dist3 or dist3 == dist1:
        return "Triangle isosceles"
    else:
        return "Triangle escale"
            

import doctest

doctest.testmod()