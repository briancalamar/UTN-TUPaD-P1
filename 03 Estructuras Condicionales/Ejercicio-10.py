# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos)
# Invierno Verano

# Desde el 21 de marzo hasta el 20 de junio
# (incluidos)
# Primavera Otoño

# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos)
# Verano Invierno

# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos)
# Otoño Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio (N/S): ").lower()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Fecha no válida")
elif hemisferio == "s":
    if (mes == 12 and dia >= 21) or (mes <= 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes <= 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes <= 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes <= 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Fecha no válida")
else:
    print("Hemisferio no válido")
