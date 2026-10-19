# Ejercicio 8.3: Gestión de eventos

import math
import tkinter as tk
from tkinter import messagebox

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def setVolumen(self, volumen):
        self.volumen = volumen

    def setSuperficie(self, superficie):
        self.superficie = superficie

    def getVolumen(self):
        return self.volumen

    def getSuperficie(self):
        return self.superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcularSuperficie(self):
        areaLadoA = 2 * math.pi * self.radio * self.altura
        areaLadoB = 2 * math.pi * self.radio ** 2
        return areaLadoA + areaLadoB

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcularSuperficie(self):
        return 4 * math.pi * self.radio ** 2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcularSuperficie(self):
        areaBase = self.base ** 2
        areaLado = 2 * self.base * self.apotema
        return areaBase + areaLado

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return self.lado ** 3

    def calcularSuperficie(self):
        return 6 * self.lado ** 2

class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.setVolumen(self.calcularVolumen())
        self.setSuperficie(self.calcularSuperficie())

    def calcularVolumen(self):
        return self.largo * self.ancho * self.altura

    def calcularSuperficie(self):
        return 2 * (
            self.largo * self.ancho
            + self.largo * self.altura
            + self.ancho * self.altura
        )

class VentanaCalculo(tk.Toplevel):
    def __init__(self, parent, titulo, campos, figura, dibujo):
        super().__init__(parent)

        self.title(titulo)
        self.geometry("440x270")
        self.resizable(False, False)

        self.campos = {}
        self.figura = figura

        self.centrarVentana()

        for i, (nombre, etiqueta) in enumerate(campos):
            y = 25 + i * 35

            tk.Label(
                self, text=etiqueta
            ).place(x=15, y=y, width=95, height=23)

            entrada = tk.Entry(self)
            entrada.place(x=110, y=y, width=95, height=23)

            self.campos[nombre] = entrada

        botonY = 25 + len(campos) * 35 + 10

        tk.Button(
            self,
            text="Calcular",
            command=self.actionPerformed,
            bg="#4CAF52"
        ).place(x=45, y=botonY, width=140, height=25)

        if dibujo in ("cilindro", "esfera", "cubo"):
            anchoResultados = 200
        else:
            anchoResultados = 400

        self.volumen = tk.Label(
            self, text="Volumen (cm3):", anchor="w"
        )
        self.volumen.place(
            x=15,
            y=botonY + 40,
            width=anchoResultados,
            height=23
        )

        self.superficie = tk.Label(
            self, text="Superficie (cm2):", anchor="w"
        )
        self.superficie.place(
            x=15,
            y=botonY + 70,
            width=anchoResultados,
            height=23
        )

        self.canvas = tk.Canvas(
            self,
            width=190,
            height=155,
            bg="white",
            highlightthickness=1,
            highlightbackground="#cccccc"
        )
        self.canvas.place(x=225, y=25)

        getattr(self, "dibujar_" + dibujo)()

    def centrarVentana(self):
        self.update_idletasks()
        ancho = 440
        alto = 270

        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def actionPerformed(self):
        try:
            valores = [
                float(entrada.get())
                for entrada in self.campos.values()
            ]

            if any(
                not math.isfinite(valor) or valor <= 0
                for valor in valores
            ):
                raise ValueError

            figura = self.figura(*valores)

            self.volumen.config(
                text=f"Volumen (cm3): {figura.getVolumen():.2f}"
            )

            self.superficie.config(
                text=f"Superficie (cm2): {figura.getSuperficie():.2f}"
            )

        except (ValueError, OverflowError):
            messagebox.showerror(
                "Error",
                "Ingrese valores numéricos válidos y mayores que 0."
            )

    #Imagenes

    def dibujar_cilindro(self):
        c = self.canvas

        c.create_rectangle(
            50, 50, 145, 115,
            fill="#bfdbfe", outline=""
        )
        c.create_oval(
            50, 35, 145, 65,
            fill="#dbeafe", outline="#2563eb", width=2
        )
        c.create_line(
            50, 50, 50, 115,
            fill="#2563eb", width=2
        )
        c.create_line(
            145, 50, 145, 115,
            fill="#2563eb", width=2
        )
        c.create_oval(
            50, 100, 145, 130,
            outline="#2563eb", width=2
        )

    def dibujar_esfera(self):
        c = self.canvas

        c.create_oval(
            52, 30, 142, 120,
            fill="#bfdbfe", outline="#2563eb", width=2
        )
        c.create_oval(
            52, 57, 142, 91,
            outline="#2563eb", width=2, dash=(5, 3)
        )
        c.create_oval(
            78, 30, 116, 120,
            outline="#2563eb", width=2
        )

    def dibujar_piramide(self):
        c = self.canvas

        c.create_polygon(
            95, 20, 35, 115, 95, 140,
            fill="#bfdbfe", outline="#2563eb", width=2
        )
        c.create_polygon(
            95, 20, 155, 115, 95, 140,
            fill="#60a5fa", outline="#2563eb", width=2
        )
        c.create_polygon(
            35, 115, 95, 95, 155, 115, 95, 140,
            fill="#dbeafe", outline="#2563eb", width=2
        )
        c.create_line(
            95, 20, 95, 95,
            fill="#2563eb", width=2
        )

    def dibujar_cubo(self):
        c = self.canvas

        c.create_polygon(
            45, 55, 75, 35, 145, 35, 115, 55,
            fill="#dbeafe", outline="#2563eb", width=2
        )
        c.create_polygon(
            115, 55, 145, 35, 145, 105, 115, 125,
            fill="#60a5fa", outline="#2563eb", width=2
        )
        c.create_polygon(
            45, 55, 115, 55, 115, 125, 45, 125,
            fill="#bfdbfe", outline="#2563eb", width=2
        )

    def dibujar_prisma(self):
        c = self.canvas

        c.create_polygon(
            30, 60, 55, 40, 155, 40, 130, 60,
            fill="#dbeafe", outline="#2563eb", width=2
        )
        c.create_polygon(
            130, 60, 155, 40, 155, 110, 130, 130,
            fill="#60a5fa", outline="#2563eb", width=2
        )
        c.create_polygon(
            30, 60, 130, 60, 130, 130, 30, 130,
            fill="#bfdbfe", outline="#2563eb", width=2
        )

#Figuras

class VentanaCilindro(VentanaCalculo):
    def __init__(self, parent):
        super().__init__(
            parent,
            "Cilindro",
            [
                ("radio", "Radio (cm):"),
                ("altura", "Altura (cm):")
            ],
            Cilindro,
            "cilindro"
        )

class VentanaEsfera(VentanaCalculo):
    def __init__(self, parent):
        super().__init__(
            parent,
            "Esfera",
            [
                ("radio", "Radio (cm):")
            ],
            Esfera,
            "esfera"
        )

class VentanaPiramide(VentanaCalculo):
    def __init__(self, parent):
        super().__init__(
            parent,
            "Pirámide",
            [
                ("base", "Base (cm):"),
                ("altura", "Altura (cm):"),
                ("apotema", "Apotema (cm):")
            ],
            Piramide,
            "piramide"
        )

class VentanaCubo(VentanaCalculo):
    def __init__(self, parent):
        super().__init__(
            parent,
            "Cubo",
            [
                ("lado", "Lado (cm):")
            ],
            Cubo,
            "cubo"
        )

class VentanaPrisma(VentanaCalculo):
    def __init__(self, parent):
        super().__init__(
            parent,
            "Prisma rectangular",
            [
                ("largo", "Largo (cm):"),
                ("ancho", "Ancho (cm):"),
                ("altura", "Altura (cm):")
            ],
            Prisma,
            "prisma"
        )

#Principal

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Figuras geométricas")
        self.geometry("520x160")
        self.resizable(False, False)

        self.centrarVentana()

        tk.Label(
            self,
            text="Seleccione una figura geométrica:",
            font=("Arial", 12)
        ).place(x=100, y=20, width=320, height=25)

        tk.Button(
            self,
            text="Cilindro",
            command=self.abrirCilindro
        ).place(x=15, y=65, width=90, height=30)

        tk.Button(
            self,
            text="Esfera",
            command=self.abrirEsfera
        ).place(x=115, y=65, width=90, height=30)

        tk.Button(
            self,
            text="Pirámide",
            command=self.abrirPiramide
        ).place(x=215, y=65, width=90, height=30)

        tk.Button(
            self,
            text="Cubo",
            command=self.abrirCubo
        ).place(x=315, y=65, width=90, height=30)

        tk.Button(
            self,
            text="Prisma",
            command=self.abrirPrisma
        ).place(x=415, y=65, width=90, height=30)

    def centrarVentana(self):
        self.update_idletasks()

        ancho = 520
        alto = 160

        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def abrirCilindro(self):
        VentanaCilindro(self)

    def abrirEsfera(self):
        VentanaEsfera(self)

    def abrirPiramide(self):
        VentanaPiramide(self)

    def abrirCubo(self):
        VentanaCubo(self)

    def abrirPrisma(self):
        VentanaPrisma(self)

class Principal:
    @staticmethod
    def main():
        miVentanaPrincipal = VentanaPrincipal()
        miVentanaPrincipal.mainloop()

if __name__ == "__main__":
    Principal.main()