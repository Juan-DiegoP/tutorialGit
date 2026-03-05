from src.services.sistema_cine import SistemaCine

def mostrar_cartelera(sistema: SistemaCine):
    print("\n=== CARTELERA ===")
    for i, func in enumerate(sistema.listar_cartelera(), start=1):
        # usa getters que agregaste en Funcion
        print(f"{i}. [{func.codigo}] {func.titulo} - Sala {func.sala} - {func.horario}")

def mostrar_menu_confiteria(sistema: SistemaCine):
    print("\n=== MENÚ CONFITERÍA ===")
    for prod in sistema.listar_menu_confiteria():
        print(prod.info_basica())

def menu_principal():
    sistema = SistemaCine()

    while True:
        print("\n===== SISTEMA DE CINE =====")
        print("1. Ver cartelera")
        print("2. Vender entrada general")
        print("3. Ver menú confitería")
        print("4. Vender producto confitería")
        print("5. Ver reporte de ingresos")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            mostrar_cartelera(sistema)

        elif opcion == "2":
            mostrar_cartelera(sistema)
            try:
                idx = int(input("Número de función: ")) - 1
                funcion = sistema.listar_cartelera()[idx]
            except (ValueError, IndexError):
                print("Función inválida")
                continue

            asiento = input("Asiento (ej. A1): ")
            dia = input("Día de la semana: ")
            try:
                hora = int(input("Hora (entero, ej. 18, 20): "))
            except ValueError:
                print("Hora inválida")
                continue

            ok, resultado = sistema.vender_entrada_general(funcion, asiento, dia, hora)
            if ok:
                entrada = resultado
                print(f"\nEntrada vendida correctamente.")
                print(f"Tipo: {entrada.__class__.__name__}")
                print(f"Total a pagar: ${entrada.calcular_precio_final():.2f}")
            else:
                print("No se pudo vender la entrada:", resultado)

        elif opcion == "3":
            mostrar_menu_confiteria(sistema)

        elif opcion == "4":
            mostrar_menu_confiteria(sistema)
            codigo = input("Código de producto: ")
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida")
                continue

            ok, resultado = sistema.vender_producto_confiteria(codigo, cantidad)
            if ok:
                prod = resultado
                print(f"\nVenta realizada: {prod.nombre} x{cantidad}")
            else:
                print("No se pudo realizar la venta:", resultado)

        elif opcion == "5":
            rep = sistema.obtener_reporte_ingresos()
            print("\n=== INGRESOS ===")
            print(f"Ingresos por taquilla:   ${rep['taquilla']:.2f}")
            print(f"Ingresos confitería:     ${rep['confiteria']:.2f}")
            print(f"TOTAL:                   ${rep['total']:.2f}")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()