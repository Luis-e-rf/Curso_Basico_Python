def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos  = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu  = """
Bienvenidos al conversor de monedas 🪙

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4040)
elif opcion == 2:
    conversor("argentinos", 103.3)
elif opcion == 3:
    conversor("mexicanos", 20.4)
else:
    print('Ingresa una opción correcta por favor')
