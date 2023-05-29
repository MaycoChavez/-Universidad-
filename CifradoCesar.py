'''
Integrantes : Mayco Chavez, Agustin Davila, Nicolas Gutierrez
'''
#Diccionario de palabras en inglés
from diccionario import arreglo_palabras

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']


def menu():
    print('1. Cifrar')
    print('2. Desifrar')
    print('3. Fuerza bruta(debe ser una palabra o frase ----CIFRADA----)') 
    print('S. Salir')
    op = input('Elija una opcion: ').upper()
    while op != 'S':
        if op == '1':
            frase = input('Ingrese la frase a CODIFICAR: ')
            x = int(input('Ingrese el numero de DESPLAZAMIENTO: '))
            cifrar(frase, x)
            menu()
            break
        elif op == '2':
            frase = input('Ingrese la frase a DECIFRAR: ')
            x = int(input('Ingrese el numero de DESPLAZAMIENTO: '))
            descifrado(frase, x)
            menu()
            break
        elif op == '3':
            frase = input('Ingrese la frase a CRACKEAR: ')
            crackeador(frase)
            menu()
            break
        else:
            print('Opcion Incorrecta')
            menu()
            break
        
    
        
    

#----------------------- PUNTO 1 ----------------------------------------- 
def cifrar(fr, x):# fr = frase, x = numero de despazamiento 
    cifrado = ''
    #Buscamos el elemento x desde su posicion hasta el final y luego desde el comienzo hasta su posicion 
    aux = alfabeto[x:] + alfabeto[:x]
    for letra in fr:
        #Obtenemos en que lugar esta la letra en el alfabeto 
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            cifrado += aux[indice]
        else:
            cifrado += letra
    print(cifrado)




#----------------------- PUNTO 2 -----------------------------------------
def descifrado(fr, x):
    texto_descifrado = ''
    aux = alfabeto[x:] + alfabeto[:x]
    
    for letra in fr:
        if letra in aux:
            indice = aux.index(letra)
            texto_descifrado += alfabeto[indice]
        else:
            texto_descifrado += letra 
    print(texto_descifrado)





#----------------------- PUNTO 3 -----------------------------------------

def crackeador(texto_cifrado):

    for desplazamiento in range(1, len(alfabeto)):
        texto_descifrado = ''
        aux = alfabeto[desplazamiento:] + alfabeto[:desplazamiento]

        for letra in texto_cifrado:
            if letra in aux:
                indice = aux.index(letra)
                texto_descifrado += alfabeto[indice]
            else:
                texto_descifrado += letra

        # Verificar si las palabras del texto descifrado están en el diccionario
        palabras = texto_descifrado.split()
        
        palabras_validas = [palabra for palabra in palabras if palabra.lower() in arreglo_palabras]
        if len(palabras) == 1 and len(palabras_validas) > 0:
            print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")
        elif  len(palabras) > 1 and len(palabras_validas) > 1:
            print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")

            

menu()
