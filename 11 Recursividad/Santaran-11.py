# # 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# # función para calcular y mostrar en pantalla el factorial de todos los números enteros
# # entre 1 y el número que indique el usuario

# ## Funcion recursiva para calcular el factorial
# def calcular_factorial(numero):
#     if numero <= 0:
#         return 0
#     elif numero == 1:
#         return 1
#     else:
#         return numero * calcular_factorial(numero - 1)

# ## Funcion recursiva para calcular el factorial de todos los numeros del 1 al "numero" ingresado
# def calcular_factoriales(numero):
#     if numero <= 0:
#         print(0)
#     elif numero == 1:
#         print(1)
#     else:
#         print(calcular_factorial(numero))
#         calcular_factoriales(numero - 1)
        
# numero = int(input('Ingrese un numero positivo: '))
# calcular_factoriales(numero)

# # 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# # indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# # especifique.

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# def mostrar_fibonacci(n):
#     if n < 0:
#         print("Ingrese un numero positivo")
#     else:
#         for i in range(n):
#             print(fibonacci(i), end=' ')
#         print()

# numero_fibonacci = int(input('Ingrese la posicion de la serie de Fibonacci: '))
# mostrar_fibonacci(numero_fibonacci)

# # 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# # exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general

# def potencia(base, exponente):
#     if exponente < 0:
#         return 1 / potencia(base, -exponente) # Manejo de exponentes negativos
#     elif exponente == 0:
#         return 1
#     else:
#         return base * potencia(base, exponente - 1) # Recursión para calcular la potencia

# def calcular_potencia():
#     base = int(input('Ingrese la base: '))
#     exponente = int(input('Ingrese el exponente: '))
#     resultado = potencia(base, exponente)
#     print(f'{base} elevado a {exponente} es {resultado}')

# calcular_potencia()

# # 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# # decimal y devuelva su representación en binario como una cadena de texto.
# # Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# # unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# # procedimiento:

# # 1. Dividir el número por 2.
# # 2. Guardar el resto (0 o 1).
# # 3. Repetir el proceso con el cociente hasta que llegue a 0.
# # 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

# def decimal_a_binario(numero):
#     if numero == 0:
#         return '0'
#     else:
#         return decimal_a_binario(numero // 2) + str(numero % 2) # Recursión para construir el binario

# decimal = int(input('Ingrese un numero entero positivo: '))
# binario = decimal_a_binario(decimal)
# print(f'El numero {decimal} en binario es: {binario}')

# # 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# # cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# # lo es.

# def es_palindromo(palabra):
#     palabra = palabra.lower()  # Convertir a minúsculas para evitar problemas de mayúsculas
#     if len(palabra) <= 1:
#         return True
#     if palabra[0] != palabra[-1]:
#         return False
#     return es_palindromo(palabra[1:-1])  # Llamada recursiva con la subcadena sin los extremos

# # 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# # número entero positivo y devuelva la suma de todos sus dígitos.

# def suma_digitos(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + suma_digitos(n // 10)  # Sumar el último dígito y llamar recursivamente con el resto
    
# numero = int(input('Ingrese un numero entero positivo: '))
# resultado_suma = suma_digitos(numero)
# print(f'La suma de los dígitos de {numero} es: {resultado_suma}')

# # 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# # bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# # último nivel con un solo bloque.
# # Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# # nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# # pirámide.

# def contar_bloques(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + contar_bloques(n - 1)  # Sumar el nivel actual y llamar recursivamente con el nivel anterior

# numero_bloques = int(input('Ingrese el número de bloques en el nivel más bajo: '))
# total_bloques = contar_bloques(numero_bloques)
# print(f'El total de bloques necesarios para construir la pirámide es: {total_bloques}')

# # 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# # número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# # aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0  # Si el número es 0, solo cuenta si el dígito es 0
    elif numero < 10:
        return 1 if numero == digito else 0  # Si el número es un solo dígito, compara directamente
    else:
        consulta_actual = 1 if numero % 10 == digito else 0  # Verifica el último dígito
        return consulta_actual + contar_digito(numero // 10, digito)  # Contar el dígito y llamar recursivamente

numero = int(input('Ingrese un número entero positivo: '))
digito = int(input('Ingrese un dígito (0-9): '))
resultado_contar = contar_digito(numero, digito)
print(f'El dígito {digito} aparece {resultado_contar} veces en el número {numero}.')

