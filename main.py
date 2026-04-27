from cliente import Cliente

try:
    cliente1 = Cliente ("123456", "Juan", "Daza")

    print(cliente1.mostrar_informacion())
except Exception as e:
    print("❌Error", e)