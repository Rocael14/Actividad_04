def MenuMedicamento():
    print("1. Agregar Medicamento")
    print("2. Entregar Medicamento")
    print("3. Mostrar Medicamentos")
    print("4. Salir")

medicamento = []
while True:
    MenuMedicamento()
    try:
        opcion = int(input("Selecciona una opcion: "))
        match opcion:
            case 1:
                print("Agregar Medicamento")
                nombre = input("Ingrese el nombre del medicamento: ").strip().capitalize()
                medicamento.append(nombre)
                print(f"¡{nombre} agregado a la lista!")
            case 2:
                print("Entregar Medicamento")
            case 3:
                print("Mostrar Medicamentos")
            case 4:
                print("Gracias por usar el sistema de farmacia")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")
    except ValueError:
        print("Ingreso una opcion no valida")
        continue