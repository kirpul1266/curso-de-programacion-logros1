# Programa de gestión de una biblioteca de libros

biblioteca = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar un nuevo libro")
    print("2. Mostrar los libros de la biblioteca")
    print("3. Eliminar un libro")
    print("4. Buscar libros por categoría")
    print("5. Renunciar (salir)")

def agregar_libro():
    nombre = input("Nombre del libro: ")
    categoria = input("Categoría del libro: ")
    try:
        copias = int(input("¿Cuántas copias de este libro?: "))
        if copias < 1:
            print("Debe haber al menos una copia.")
            return
    except ValueError:
        print("Número de copias inválido.")
        return
    biblioteca.append({'nombre': nombre, 'categoria': categoria, 'copias': copias})
    print(f"'{nombre}' agregado a la biblioteca con {copias} copia(s).")

def mostrar_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        print("\nLibros en la biblioteca:")
        indice = 1
        for libro in biblioteca:
            print(f"{indice}. {libro['nombre']} - Categoría: {libro['categoria']} - Copias: {libro['copias']}")
            indice += 1

def eliminar_libro():
    mostrar_biblioteca()
    if biblioteca:
        try:
            idx = int(input("Ingrese el número del libro a eliminar: "))
            if 1 <= idx <= len(biblioteca):
                libro = biblioteca[idx - 1]
                if libro['copias'] > 1:
                    libro['copias'] -= 1
                    print(f"Se eliminó una copia de '{libro['nombre']}'. Quedan {libro['copias']}.")
                else:
                    eliminado = biblioteca.pop(idx - 1)
                    print(f"'{eliminado['nombre']}' eliminado de la biblioteca.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

def buscar_por_categoria():
    categoria = input("Ingrese la categoría a buscar: ")
    encontrados = [libro for libro in biblioteca if libro['categoria'].lower() == categoria.lower()]
    if encontrados:
        print(f"\nLibros en la categoría '{categoria}':")
        for libro in encontrados:
            print(f"- {libro['nombre']}")
    else:
        print(f"No se encontraron libros en la categoría '{categoria}'.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_libro()
        elif opcion == '2':
            mostrar_biblioteca()
        elif opcion == '3':
            eliminar_libro()
        elif opcion == '4':
            buscar_por_categoria()
        elif opcion == '5':
            print("¡Gracias por usar la biblioteca!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
1