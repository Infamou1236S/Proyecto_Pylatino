import pandas as pandas_libreria
from datetime import datetime

"""Estructura de los datos"""

lista_habitos_registrados = [] 
historial_registros_habitos = [] 

"""Funciones principales"""
def agregar_nuevo_habito():
    nombre_habito_ingresado = input("Ingrese el nombre del hábito que desea agregar: ").strip()

    if nombre_habito_ingresado:
        if nombre_habito_ingresado in lista_habitos_registrados:
            print("Este hábito ya existe.")
        else:
            lista_habitos_registrados.append(nombre_habito_ingresado)
            print(f"Hábito '{nombre_habito_ingresado}' agregado correctamente.")
    else:
        print("Nombre de hábito no válido.")

def eliminar_habito_existente():
    if not lista_habitos_registrados:
        print("No hay hábitos para eliminar.")
        return

    print("\n--- HÁBITOS REGISTRADOS ---")
    for indice, habito in enumerate(lista_habitos_registrados, start=1):
        print(f"{indice}. {habito}")

    try:
        numero_habito = int(input("Seleccione el número del hábito que desea eliminar: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if numero_habito < 1 or numero_habito > len(lista_habitos_registrados):
        print("Número fuera de rango.")
        return

    habito_a_eliminar = lista_habitos_registrados[numero_habito - 1]

    lista_habitos_registrados.remove(habito_a_eliminar)

    global historial_registros_habitos
    historial_registros_habitos = [
        registro for registro in historial_registros_habitos
        if registro["nombre_habito"] != habito_a_eliminar
    ]

    print(f"Hábito '{habito_a_eliminar}' eliminado correctamente.")

def registrar_cumplimiento_diario_habitos():
    if not lista_habitos_registrados:
        print("No hay hábitos registrados todavía.")
        return

    fecha_actual_registro = datetime.now().strftime("%Y-%m-%d")
    print(f"\nFecha del registro: {fecha_actual_registro}")
    print("Responda si cumplió los hábitos (s/n):")

    for habito_en_lista in lista_habitos_registrados:
        respuesta_cumplimiento = input(f"¿Cumplió el hábito '{habito_en_lista}'? (s/n): ").lower()
        habito_cumplido = True if respuesta_cumplimiento == "s" else False

        historial_registros_habitos.append({
            "fecha_registro": fecha_actual_registro,
            "nombre_habito": habito_en_lista,
            "habito_cumplido": habito_cumplido
        })

    print("\nCumplimiento diario registrado exitosamente.")

def mostrar_historial_completo_habitos():
    if not historial_registros_habitos:
        print("No hay registros en el historial aún.")
        return
    
    print("\n--- HISTORIAL COMPLETO DE HÁBITOS ---")
    for registro in historial_registros_habitos:
        texto_estado_habito = "Cumplido" if registro["habito_cumplido"] else "No cumplido"
        print(f"{registro['fecha_registro']} - {registro['nombre_habito']}: {texto_estado_habito}")

def exportar_historial_a_dataframe():
    if not historial_registros_habitos:
        print("No hay historial disponible para convertir a DataFrame.")
        return None
    
    dataframe_historial_habitos = pandas_libreria.DataFrame(historial_registros_habitos)

    print("\nDataFrame generado correctamente:")
    print(dataframe_historial_habitos)

    return dataframe_historial_habitos

def mostrar_resumen_semanal_habitos():
    dataframe_historial_habitos = exportar_historial_a_dataframe()

    if dataframe_historial_habitos is None:
        return
    
    print("\n--- RESUMEN SEMANAL DE CUMPLIMIENTO ---")

    resumen_semanal_habitos = (
        dataframe_historial_habitos.groupby("nombre_habito")["habito_cumplido"]
        .mean()
        .reset_index()
        .rename(columns={"habito_cumplido": "porcentaje_cumplimiento"})
    )

    resumen_semanal_habitos["porcentaje_cumplimiento"] *= 100

    print(resumen_semanal_habitos)

"""Menú principal"""
def iniciar_menu_principal():
    opcion = "0"

    while opcion != "7":
        print("\n========== MENÚ DEL SISTEMA DE SEGUIMIENTO DE HÁBITOS ==========")
        print("1. Agregar nuevo hábito")
        print("2. Registrar cumplimiento diario")
        print("3. Ver historial de hábitos")
        print("4. Ver resumen semanal")
        print("5. Exportar historial")
        print("6. Eliminar hábito")
        print("7. Salir del programa")

        opcion = input("Seleccione una opción del menú: ")

        if opcion == "1":
            agregar_nuevo_habito()
        elif opcion == "2":
            registrar_cumplimiento_diario_habitos()
        elif opcion == "3":
            mostrar_historial_completo_habitos()
        elif opcion == "4":
            mostrar_resumen_semanal_habitos()
        elif opcion == "5":
            exportar_historial_a_dataframe()
        elif opcion == "6":
            eliminar_habito_existente()
        elif opcion == "7":
            print("Saliendo del sistema de hábitos...")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

iniciar_menu_principal()


