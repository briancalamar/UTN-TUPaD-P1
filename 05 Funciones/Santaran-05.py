import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print('Hola Mundo!')

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f'Hola {nombre}!'

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):    
    return 2 * math.pi * radio

radio = int(input('Ingrese el radio de un circulo: '))
print(f'El area es: {calcular_area_circulo}')
print(f'El perimetro es: {calcular_perimetro_circulo}')

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    segundos_por_minuto = 60
    minutos_por_hora = 60
    return segundos / ( segundos_por_minuto * minutos_por_hora )

segundos = int(input('Ingrese un numero de segundos: '))

print(f'Los segundos ingresados son {segundos_a_horas(segundos)} horas')


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(i * numero)

numero_para_tabla = int(input('Ingresa un numero: '))
tabla_multiplicar(numero_para_tabla)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    tupla = f'Suma: {a + b}', f'Resta: {a - b}', f'Multiplicacion: {a * b}', f'Division: {a / b}'
    return tupla

print(operaciones_basicas(10, 5))


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / ( altura ** 2 )

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return ((9 / 5) * celsius ) + 32

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    return suma / 3

numero_uno = int(input('1/3 - Ingrese un numero: '))
numero_dos = int(input('2/3 - Ingrese un numero: '))
numero_tres = int(input('3/3 - Ingrese un numero: '))

print(f'El promedio de los tres es: {calcular_promedio(numero_uno, numero_dos, numero_tres)}')


def funcion_principal():
    imprimir_hola_mundo()
    
    nombre = input('Ingresa tu nombre: ')
    apellido = input('Ingresa tu apellido: ')
    edad = input('Ingresa tu edad: ')
    peso = int(input('Ingresa tu peso: '))
    altura = int(input('Ingresa tu altura: '))
    residencia = input('Ingresa tu residencia: ')
    temperatura_en_celsius = int(input('Ingresa la temperatura actual en celsius: '))
    
    print(saludar_usuario(nombre))
    print(informacion_personal(nombre, apellido, edad, residencia))
    print(calcular_imc(peso, altura))
    print(celsius_a_fahrenheit(temperatura_en_celsius))


    



funcion_principal()