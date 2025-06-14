# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios

frutas = list(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input(f'Ingrese el nombre del contacto {i + 1}: ')
    numero = input(f'Ingrese el numero de telefono de {nombre}: ')
    contactos[nombre] = numero

nombre_consulta = input('Ingrese el nombre del contacto a consultar: ')

if nombre_consulta in contactos:
    print(f'El numero de telefono de {nombre_consulta} es: {contactos[nombre_consulta]}')
else:
    print(f'No se encontro el contacto {nombre_consulta} en la lista.')

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input('Ingrese una frase: ')
palabras = frase.split()
palabras_unicas = set(palabras)
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1
print('Palabras únicas:', palabras_unicas)
print('Conteo de palabras:', conteo_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre_alumno = input(f'Ingrese el nombre del alumno {i + 1}: ')
    notas = []
    for j in range(3):
        nota = float(input(f'Ingrese la nota {j + 1} de {nombre_alumno}: '))
        notas.append(nota)
    alumnos[nombre_alumno] = tuple(notas)

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {101, 102, 103, 104}
parcial_2 = {103, 104, 105, 106}

# Estudiantes que aprobaron ambos parciales
aprobados_ambos = parcial_1.intersection(parcial_2)
print('Estudiantes que aprobaron ambos parciales:', aprobados_ambos)

# Estudiantes que aprobaron solo uno de los dos
aprobados_solo_uno = parcial_1.symmetric_difference(parcial_2)
print('Estudiantes que aprobaron solo uno de los dos parciales:', aprobados_solo_uno)

# Estudiantes que aprobaron al menos un parcial (sin repetir)
aprobados_total = parcial_1.union(parcial_2)
print('Estudiantes que aprobaron al menos un parcial:', aprobados_total)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

productos_stock = {}
def consultar_stock(producto):
    return productos_stock.get(producto, 'Producto no encontrado.')

def agregar_stock(producto, unidades):
    if producto in productos_stock:
        productos_stock[producto] += unidades
        return f'Se han agregado {unidades} unidades al stock de {producto}.'
    else:
        return 'Producto no encontrado en el stock.'

def agregar_producto(producto, unidades):
    if producto not in productos_stock:
        productos_stock[producto] = unidades
        return f'Se ha agregado el producto {producto} con {unidades} unidades al stock.'
    else:
        return 'El producto ya existe en el stock.'

continuar_en_menu = True

while continuar_en_menu:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto al stock")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        producto_consulta = input('Ingrese el nombre del producto a consultar: ')
        print(consultar_stock(producto_consulta))
    elif opcion == '2':
        producto_existente = input('Ingrese el nombre del producto existente: ')
        unidades = int(input('Ingrese la cantidad de unidades a agregar: '))
        print(agregar_stock(producto_existente, unidades))
    elif opcion == '3':
        nuevo_producto = input('Ingrese el nombre del nuevo producto: ')
        unidades_nuevo = int(input('Ingrese la cantidad de unidades del nuevo producto: '))
        print(agregar_producto(nuevo_producto, unidades_nuevo))
    elif opcion == '4':
        continuar_en_menu = False
    else:
        print('Opción no válida, por favor intente nuevamente.')


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos

agenda = {}
def agregar_evento(dia, hora, evento):
    clave = (dia, hora)
    if clave in agenda:
        return f'Ya existe un evento en {clave}.'
    else:
        agenda[clave] = evento
        return f'Evento "{evento}" agregado para {clave}.'

def consultar_evento(dia, hora):
    clave = (dia, hora)
    return agenda.get(clave, 'No hay evento programado para ese día y hora.')

continuar_en_menu = True

while continuar_en_menu:
    print("\nOpciones:")
    print("1. Agregar evento")
    print("2. Consultar evento")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        dia = input('Ingrese el día del evento (ejemplo: Lunes): ')
        hora = input('Ingrese la hora del evento (ejemplo: 10:00 AM): ')
        evento = input('Ingrese el nombre del evento: ')
        print(agregar_evento(dia, hora, evento))
    elif opcion == '2':
        dia_consulta = input('Ingrese el día a consultar: ')
        hora_consulta = input('Ingrese la hora a consultar: ')
        print(consultar_evento(dia_consulta, hora_consulta))
    elif opcion == '3':
        continuar_en_menu = False
    else:
        print('Opción no válida, por favor intente nuevamente.')

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma'
}

paises = paises_capitales.keys()
capitales = paises_capitales.values()

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
print('Diccionario de capitales y países:', capitales_paises)