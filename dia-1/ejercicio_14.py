#Cajero automático: 
"""
Crea un cajero con un saldo inicial de $500.000 y estas opciones:

    Consultar saldo.
    Retirar dinero.
    Depositar dinero.
    Salir.

Valida las operaciones y actualiza el saldo.
"""

saldoInicial = 500000

print("***Bienvenido a cajerin***")
print("\n***Por favor elige una opción***")
print("\n1-Consultar saldo \n2-Retirar dinero \n3-Depositar dinero \n4-Salir")

opcion = int(input("Opción: "))

if opcion == 1:
    print("\nSu saldo actual es: $", saldoInicial)
elif opcion == 2:
    retiro = float(input("\n¿Cuánto dinero desea retirar?: $"))
    nuevoSaldo = saldoInicial - retiro
    print("Señor usuario, usted retiro $", retiro, "\nSu saldo actual es: $", nuevoSaldo)
elif opcion == 3:
    deposito = float(input("\n¿Cuánto dinero desea depositar?: $"))
    nuevoSaldo = saldoInicial + deposito
    print("Señor usuario, usted deposito: $",deposito, "\nSu saldo actual es: $", nuevoSaldo)
elif opcion == 4:
    print("\nUn gusto servirle")
else:
    print("\nOpción elegida no valida")