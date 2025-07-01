# Programa de gestión de un carrito de compras

carrito = []

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar un nuevo producto")
    print("2. Mostrar productos en el carrito")
    print("3. Eliminar un producto")
    print("4. Buscar productos por categoría")
    print("5. Renunciar (salir)")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo.")
            return
    except ValueError:
        print("Precio inválido.")
        return
    carrito.append({'nombre': nombre, 'categoria': categoria, 'precio': precio})
    print(f"'{nombre}' agregado al carrito por ${precio:.2f}.")

def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
    else:
        print("\nProductos en el carrito:")
        total = 0
        for idx, producto in enumerate(carrito, 1):
            print(f"{idx}. {producto['nombre']} - Categoría: {producto['categoria']} - Precio: ${producto['precio']:.2f}")
            total += producto['precio']
        print(f"Total: ${total:.2f}")

def eliminar_producto():
    mostrar_carrito()
    if carrito:
        try:
            idx = int(input("Ingrese el número del producto a eliminar: "))
            if 1 <= idx <= len(carrito):
                eliminado = carrito.pop(idx - 1)
                print(f"'{eliminado['nombre']}' eliminado del carrito.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

def buscar_por_categoria():
    categoria = input("Ingrese la categoría a buscar: ")
    encontrados = [p for p in carrito if p['categoria'].lower() == categoria.lower()]
    if encontrados:
        print(f"\nProductos en la categoría '{categoria}':")
        for producto in encontrados:
            print(f"- {producto['nombre']} (${producto['precio']:.2f})")
    else:
        print(f"No se encontraron productos en la categoría '{categoria}'.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_carrito()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            buscar_por_categoria()
        elif opcion == '5':
            print("¡Gracias por usar el carrito de compras!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main() 