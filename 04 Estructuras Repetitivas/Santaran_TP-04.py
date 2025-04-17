# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(101):
    # print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# numero = int(input("Ingresa un numero entero: "))

# digitos = 0
# nuevoNumeroDivisible = numero

# while nuevoNumeroDivisible >= 1:
#     digitos += 1
#     nuevoNumeroDivisible = nuevoNumeroDivisible / 10
    
# print(digitos)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# primerNumero = int(input("Ingrese el primer numero entero: "))
# segundoNumero = int(input("Ingrese el segundo numero entero: "))

# suma = 0

# for i in range (primerNumero + 1, segundoNumero):
#     suma += i

# print(suma)



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# numeroIngresado = int(input("Ingrese un numero entero: "))

# suma = 0

# while numeroIngresado > 0:
#     suma += numeroIngresado
#     print(suma)

#     numeroIngresado = int(input("Ingrese otro numero entero: "))

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# from random import randint

# intentos = 1
# numeroIngresado = int(input("Ingrese numero entero entre 0 y 9: "))
# numeroAleatorio = randint(0, 9)

# while numeroIngresado != numeroAleatorio:
#     intentos += 1
#     numeroIngresado = int(input("Ingrese otro numero entero entre 0 y 9: "))

# print(f"Cantidad de intentos: {intentos}")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(98, 0, -2):
#     print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# primerNumero = 0
# segundoNumero = int(input("Ingrese un numero entero positivo: "))

# suma = 0

# for i in range (primerNumero + 1, segundoNumero):
#     suma += i

# print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# numerosAIngresar = 100
# numerosIngresados = 0
# cantidadPares = 0
# cantidadImpares = 0
# cantidadNegativos = 0
# cantidadPositivos = 0

# while numerosIngresados < numerosAIngresar:
#     numero = int(input(f"{numerosIngresados + 1} - Ingresa un numero entero: "))
#     numerosIngresados += 1

#     if numero % 2 == 0:
#         cantidadPares += 1
#     else:
#         cantidadImpares += 1
    
#     if numero > 0:
#         cantidadPositivos += 1
#     else:
#         cantidadNegativos += 1

# print(f"Numeros positivos: {cantidadPositivos}")
# print(f"Numeros negativos: {cantidadNegativos}")
# print(f"Numeros pares: {cantidadPares}")
# print(f"Numeros impares: {cantidadImpares}")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# numerosAIngresar = 10
# numerosIngresados = 0
# suma = 0

# while numerosIngresados < numerosAIngresar:
#     numero = int(input(f"{numerosIngresados + 1} - Ingresa un numero entero: "))
#     numerosIngresados += 1
#     suma += numero

# media = suma / numerosAIngresar
# print(f"La media es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero entero: ")
numeroInvertido = 0
numeroDivisible = int(numero)
digitos = len(numero)

for i in range(digitos):
    numeroInvertido += numeroDivisible % 10 * (10 ** (digitos - i - 1))
    numeroDivisible = numeroDivisible // 10

print(f"El numero invertido es: {numeroInvertido}")
