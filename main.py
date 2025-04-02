#voy a hacer un menú para elegir el ejercicio que se quiera ejecutar
from ejer1.ejer1 import resolver_puzzle
from ejer2.ejer2 import ejecutar_determinantes, matriz

def main():
    while True:
        print("\n Menú de ejercicios")
        print("Ejercicio 1")
        print("Ejercicio 2")
        print("Ejercicio 3")
        print("Ejercicio 4")
        print("Escribe 'salir' para salir")

        opcion = input("Elige una opción: ")

        if opcion.lower() == 'salir':
            print("Saliendo del programa...")
            break

        if opcion == '1':
            print("Ejecutando ejercicio 1...")
            resolver_puzzle()
        elif opcion == '2':
            print("Ejecutando ejercicio 2...")
            ejecutar_determinantes(matriz)
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        else:
            print("ERROR FATAL")


if __name__ == "__main__":
    main()