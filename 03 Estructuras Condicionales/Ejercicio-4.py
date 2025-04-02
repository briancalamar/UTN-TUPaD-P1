# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edadUsuario = int(input("Ingrese su edad"))

if edadUsuario < 12:
    print('Pertenece a Niño/a')
elif edadUsuario >= 12 and edadUsuario < 18:
    print('Pertenece a Adolescente')
elif edadUsuario >= 18 and edadUsuario < 30:
    print('Pertenece a Adulto/a joven')
else:
    print('Pertenece a Adulto/a')
