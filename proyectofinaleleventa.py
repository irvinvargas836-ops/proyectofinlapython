import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():

    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("500x520")
    reg.resizable(False, False)
    reg.configure(bg="#F4F6F9")

    # -------------------------
    # TÍTULO
    # -------------------------
    titulo = tk.Label(
        reg,
        text="📦 Registro de Productos",
        font=("Arial", 20, "bold"),
        bg="#F4F6F9",
        fg="#2C3E50"
    )
    titulo.pack(pady=20)

    # -------------------------
    # FRAME FORMULARIO
    # -------------------------
    frame_form = tk.Frame(
        reg,
        bg="white",
        bd=0,
        relief="solid"
    )
    frame_form.pack(padx=20, pady=10, fill="both")

    # -------------------------
    # ESTILO CAMPOS
    # -------------------------
    def crear_campo(texto):
        lbl = tk.Label(
            frame_form,
            text=texto,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#34495E"
        )
        lbl.pack(anchor="w", padx=20, pady=(15, 5))

        entry = tk.Entry(
            frame_form,
            font=("Arial", 12),
            bg="#ECF0F1",
            relief="flat",
            width=35
        )
        entry.pack(ipady=8, padx=20)

        return entry

    txt_id = crear_campo("ID del Producto")
    txt_desc = crear_campo("Descripción")
    txt_precio = crear_campo("Precio")
    txt_categoria = crear_campo("Categoría")

    # -------------------------
    # FUNCIÓN GUARDAR
    # -------------------------
    def guardar_producto():

        id_prod = txt_id.get().strip()
        descripcion = txt_desc.get().strip()
        precio = txt_precio.get().strip()
        categoria = txt_categoria.get().strip()

        # Validaciones
        if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
            messagebox.showwarning(
                "Campos Vacíos",
                "Por favor complete todos los campos."
            )
            return

        # Validar precio
        try:
            float(precio)
        except:
            messagebox.showerror(
                "Error",
                "El precio debe ser un número."
            )
            return

        # Guardar archivo
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ruta = os.path.join(BASE_DIR, "productos.txt")

        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{id_prod}|{descripcion}|{precio}|{categoria}\n"
            )

        messagebox.showinfo(
            "Guardado",
            "Producto registrado correctamente."
        )

        # Limpiar campos
        txt_id.delete(0, tk.END)
        txt_desc.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_categoria.delete(0, tk.END)

    # -------------------------
    # BOTÓN GUARDAR
    # -------------------------
    btn_guardar = tk.Button(
        reg,
        text="💾 Guardar Producto",
        font=("Arial", 12, "bold"),
        bg="#5C6AE9",
        fg="white",
        activebackground="#3F51D6",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=25,
        height=2,
        command=guardar_producto
    )

    btn_guardar.pack(pady=30)

# -------------------------
# FUNCIONES SECUNDARIAS
# -------------------------
def abrir_registro_ventas():
    messagebox.showinfo(
        "Registro de Ventas",
        "Aquí irá el módulo de registro de ventas."
    )

def abrir_reportes():
    messagebox.showinfo(
        "Reportes",
        "Aquí irá el módulo de reportes."
    )

def abrir_acerca_de():
    messagebox.showinfo(
        "Acerca de",
        "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0"
    )

# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - ELEVENTA")
ventana.geometry("500x650")
ventana.resizable(False, False)
ventana.configure(bg="white")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------
# LOGO
# -------------------------
try:
    logo = Image.open(os.path.join(BASE_DIR, "logo.png"))
    logo = logo.resize((180, 180))

    img_logo = ImageTk.PhotoImage(logo)

    lbl_logo = tk.Label(
        ventana,
        image=img_logo,
        bg="white"
    )
    lbl_logo.pack(pady=20)

except:
    tk.Label(
        ventana,
        text="LOGO",
        font=("Arial", 20),
        bg="white"
    ).pack(pady=20)

# -------------------------
# FRAME BOTONES
# -------------------------
frame = tk.Frame(
    ventana,
    bg="white"
)
frame.pack(pady=10)

# -------------------------
# CREAR BOTONES MODERNOS
# -------------------------
def crear_boton(texto, comando):

    btn = tk.Label(
        frame,
        text=texto,
        font=("Arial", 12, "bold"),
        fg="white",
        bg="#5C6AE9",
        width=25,
        height=2,
        cursor="hand2"
    )

    def on_enter(e):
        btn.config(bg="#3F51D6")

    def on_leave(e):
        btn.config(bg="#5C6AE9")

    def on_click(e):
        btn.config(bg="#283593")

    def on_release(e):
        btn.config(bg="#3F51D6")
        comando()

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.bind("<Button-1>", on_click)
    btn.bind("<ButtonRelease-1>", on_release)

    return btn

crear_boton(
    "📦 Registro de Productos",
    abrir_registro_productos
).pack(pady=10)

crear_boton(
    "🛒 Registro de Ventas",
    abrir_registro_ventas
).pack(pady=10)

crear_boton(
    "📊 Reportes",
    abrir_reportes
).pack(pady=10)

crear_boton(
    "ℹ️ Acerca de",
    abrir_acerca_de
).pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()