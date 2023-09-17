"""
    GDSA - Lab1 - Rafael Echevarria
"""

def parell_senar ():
    """
    1. Escriu una funció en el que l'usuari va introduint números i es va dient si el número és parell o senar. El programa acaba quan s'introdueix un zero.
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
                
def nMayor ():
    """
    2. Escriu una funció que demani a l'usuari una llista de números i que torni el número més gran d'aquesta.
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
    3. Escriu una funció que donades dues llistes imprimeixi els elements que tinguin en comú.
    
    >>> llista1 = [1, 2, 3, 4, 5]
    >>> llista2 = [3, 4, 5, 6, 7]
    >>> list_comu (llista1, llista2)
    Els elements en comú són:
    3
    4
    5
    """
    comuns1 = set(llista1)
    comuns2 = set(llista2)
    
    comuns = comuns1.intersection(comuns2)
    
    if comuns:
        print("Els elements en comú són:")
        for numero in comuns:
            print(numero)

def esPrimo (numero):
    """
    4. Escriu una funció que retorni True o False segons si un número és primer o no.
    
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

def t_Triangle ():
    """
    5. Escriu una funció que demani a l'usuari 3 punts per formar un triangle i retorni el tipus de triangle format.
    """
    punt1 = (float(input("Introdueix la x del punt 1: ")), float(input("Introdueix la y del punt 1: ")))
    punt2 = (float(input("Introdueix la x del punt 2: ")), float(input("Introdueix la y del punt 2: ")))
    punt3 = (float(input("Introdueix la x del punt 3: ")), float(input("Introdueix la y del punt 3: ")))
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
    
def factorial (num):
    """
    6. Escriu una funció que calculi el factorial d'un número.

    >>> numero = 4
    >>> resultat = factorial(numero)
    El factorial de 4 és 24
    """
    if num < 0:
        return "El factorial no està definit per a números negatius."
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for numero in range(2, num + 1):
            fact *= numero
        return print(f"El factorial de {numero} és {fact}")    

def mVocals(frase):
    """
    7. Escriu una funció que donada una frase canviï totes les vocals per '*'
    
    >>> frase = "Hola mi nombre es Rafa"
    >>> mVocals(frase)
    H*l* m* n*mbr* *s R*f*
    """
    vocals = "AEIOUaeiou"
    mod_frase = ""
    
    for char in frase:
        if char in vocals:
            mod_frase += "*"
        else:
            mod_frase += char
    return print(mod_frase)    
    
def combi(llista1, llista2):
    """
    8. Escriu una funció que donades dues llistes, les combini sense duplicat si els elements estiguin ordenats.
    
    >>> llista1 = [1, 3, 5, 7, 9]
    >>> llista2 = [3, 4, 5, 8, 10]
    >>> resultat = combi(llista1, llista2)
    [1, 3, 4, 5, 7, 8, 9, 10]
    """
    return print(sorted(list(set(llista1 + llista2))))

import doctest

doctest.testmod()