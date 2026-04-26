from cliente import Cliente

try:
    cliente1= Cliente("123", "Rosa", "Ordoñez")
    print(cliente1.mostrar_informacio())
except Exception as e:
    print("Error:", e)