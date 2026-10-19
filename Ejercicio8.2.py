#Ejercicio 8.2: Componentes swing

import tkinter as tk
from tkinter import messagebox
import statistics

def calcular_estadisticas():
    """Calcula el promedio y la desviación estándar de las notas."""
    notas_valores = []

    try:
        for entry in entradas_notas:
            valor = float(entry.get())
            if 0 <= valor <= 5:
                notas_valores.append(valor)
            else:
                messagebox.showerror("Error de Entrada", "Todas las notas deben estar entre 0 y 5.")
                return

        promedio = statistics.mean(notas_valores)

        desviacion_estandar = statistics.stdev(notas_valores)

        mayor = max(notas_valores)

        menor = min(notas_valores)

        resultado_promedio.config(text=f"Promedio: {promedio:.2f}")
        resultado_desviacion.config(text=f"Desviación Estándar: {desviacion_estandar:.2f}")
        resultado_mayor.config(text=f"Nota Mayor: {mayor:.2f}")
        resultado_menor.config(text=f"Nota Menor: {menor:.2f}")

    except ValueError:
        messagebox.showerror("Error de Entrada", "Asegúrate de ingresar números válidos en TODOS los campos de nota.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")

def limpiar_campos():
    """Limpia el contenido de todas las entradas de notas y los resultados."""
    for entry in entradas_notas:
        entry.delete(0, tk.END)

    resultado_promedio.config(text="Promedio:")
    resultado_desviacion.config(text="Desviación Estándar:")
    resultado_mayor.config(text="Nota Mayor:")
    resultado_menor.config(text="Nota Menor:")

ventana = tk.Tk()
ventana.title("Calculadora de Notas")
ventana.geometry("300x400")
ventana.resizable(False, False)

entradas_notas = []
nombres_notas = ["Nota 1", "Nota 2", "Nota 3", "Nota 4", "Nota 5"]

for i, nombre in enumerate(nombres_notas):
    tk.Label(ventana, text=f"{nombre}:").grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entrada = tk.Entry(ventana, width=15)
    entrada.grid(row=i, column=1, padx=10, pady=5)
    entradas_notas.append(entrada)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_estadisticas, bg="#4CAF52", fg="white", font=("Arial", 10, "bold"))
boton_calcular.grid(row=len(nombres_notas), column=0, pady=15, padx=10, sticky="ew")

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos, bg="#f44222", fg="white", font=("Arial", 10, "bold"))
boton_limpiar.grid(row=len(nombres_notas), column=1, pady=15, padx=10, sticky="ew")

resultado_promedio = tk.Label(ventana, text="Promedio:", font=("Arial", 10))
resultado_promedio.grid(row=len(nombres_notas) + 1, column=0, columnspan=2, pady=5, sticky="w")

resultado_desviacion = tk.Label(ventana, text="Desviación Estándar:", font=("Arial", 10))
resultado_desviacion.grid(row=len(nombres_notas) + 2, column=0, columnspan=2, pady=5, sticky="w")

resultado_mayor = tk.Label(ventana, text="Nota Mayor:", font=("Arial", 10))
resultado_mayor.grid(row=len(nombres_notas) + 3, column=0, columnspan=2, pady=5, sticky="w")

resultado_menor = tk.Label(ventana, text="Nota Menor:", font=("Arial", 10))
resultado_menor.grid(row=len(nombres_notas) + 4, column=0, columnspan=2, pady=5, sticky="w")

ventana.mainloop()