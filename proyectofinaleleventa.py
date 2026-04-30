import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - ELEVENTA")
ventana.geometry("500x600")
ventana.resizable(False, False)
ventana.configure(bg="white")  # fondo limpio

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------
# LOGO ARRIBA (SIN FONDO)
# -------------------------
try:
    logo = Image.open(os.path.join(BASE_DIR, "logo.png"))
    logo = logo.resize((180, 180))
    img_logo = ImageTk.PhotoImage(logo)

    lbl_logo = tk.Label(ventana, image=img_logo, bg="white")
    lbl_logo.pack(pady=20)
except:
    tk.Label(ventana, text="LOGO", font=("Arial", 20), bg="white").pack(pady=20)

# -------------------------
# CONTENEDOR BOTONES
# -------------------------
frame = tk.Frame(ventana, bg="white")
frame.pack(pady=10)

# -------------------------
# BOTONES
# -------------------------
def crear_boton(texto, comando):
    btn = tk.Label(
        frame,
        text=texto,
        font=("Arial", 12),
        fg="#222222",
        bg="#DDDDDD",
        width=25,
        height=2,
        bd=0
    )

    def on_enter(e):
        btn.config(bg="#41B0D1")

    def on_leave(e):
        btn.config(bg="#749DCC")

    def on_click(e):
        btn.config(bg="#C0CBEE")

    def on_release(e):
        btn.config(bg="#5C6AE9")
        comando()

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)
    btn.bind("<ButtonRelease-1>", on_release)

    return btn

crear_boton("Registro de Productos", abrir_registro_productos).pack(pady=10)
crear_boton("Registro de Ventas", abrir_registro_ventas).pack(pady=10)
crear_boton("Reportes", abrir_reportes).pack(pady=10)
crear_boton("Acerca de", abrir_acerca_de).pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()