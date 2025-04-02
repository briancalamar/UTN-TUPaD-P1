# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

wordOrPhrase = input('Ingrese una frase o palabra: ')

if len(wordOrPhrase) == 0:
    print('Debia ingresar una frase o palabra')
else:
    lastCharacter = wordOrPhrase[-1]

    if lastCharacter == 'a' or lastCharacter == 'e' or lastCharacter == 'i' or lastCharacter == 'o' or lastCharacter == 'u':
        print(f'{wordOrPhrase}!')
    else:
        print(wordOrPhrase)