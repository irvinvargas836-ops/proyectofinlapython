import tkinter as tk
from tkinter import ttk
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
from datetime import datetime

def mostrar_ticket(producto, precio, cantidad, total):

    ticket = tk.Toplevel()
    ticket.title("Ticket de Venta")
    ticket.geometry("380x520")
    ticket.resizable(False, False)
    ticket.configure(bg="white")

    # -------------------------
    # FRAME PRINCIPAL
    # -------------------------
    frame_ticket = tk.Frame(
        ticket,
        bg="white",
        bd=2,
        relief="solid"
    )
    frame_ticket.pack(padx=15, pady=15, fill="both", expand=True)

    # -------------------------
    # LOGO / IMAGEN
    # -------------------------
    try:
        ruta_logo = os.path.join(BASE_DIR, "logo_ticket.png")

        logo = Image.open(ruta_logo)
        logo = logo.resize((100, 100))

        img_logo_ticket = ImageTk.PhotoImage(logo)

        lbl_logo = tk.Label(
            frame_ticket,
            image=img_logo_ticket,
            bg="white"
        )

        lbl_logo.image = img_logo_ticket
        lbl_logo.pack(pady=(15, 5))

    except:
        lbl_logo = tk.Label(
            frame_ticket,
            text="ELEVENTA",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="#5C6AE9"
        )
        lbl_logo.pack(pady=(15, 5))

    # -------------------------
    # ENCABEZADO
    # -------------------------
    lbl_titulo = tk.Label(
        frame_ticket,
        text="PUNTO DE VENTA",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="#2C3E50"
    )
    lbl_titulo.pack()

    lbl_sub = tk.Label(
        frame_ticket,
        text="Ticket de Compra",
        font=("Arial", 11),
        bg="white",
        fg="gray"
    )
    lbl_sub.pack(pady=(0, 10))

    # -------------------------
    # FECHA Y HORA
    # -------------------------
    fecha_hora = datetime.now().strftime("%d/%m/%Y  %I:%M:%S %p")

    lbl_fecha = tk.Label(
        frame_ticket,
        text=f"Fecha: {fecha_hora}",
        font=("Consolas", 10),
        bg="white"
    )
    lbl_fecha.pack()

    separador1 = tk.Frame(frame_ticket, bg="#D5D8DC", height=2)
    separador1.pack(fill="x", padx=15, pady=10)

    # -------------------------
    # INFORMACIÓN DE VENTA
    # -------------------------
    info = [
        ("Producto", producto),
        ("Precio", f"${precio}"),
        ("Cantidad", cantidad),
        ("Total", f"${total}")
    ]

    for campo, valor in info:

        fila = tk.Frame(frame_ticket, bg="white")
        fila.pack(fill="x", padx=20, pady=5)

        lbl_campo = tk.Label(
            fila,
            text=f"{campo}:",
            font=("Arial", 11, "bold"),
            bg="white",
            anchor="w"
        )
        lbl_campo.pack(side="left")

        lbl_valor = tk.Label(
            fila,
            text=valor,
            font=("Arial", 11),
            bg="white",
            fg="#34495E"
        )
        lbl_valor.pack(side="right")

    separador2 = tk.Frame(frame_ticket, bg="#D5D8DC", height=2)
    separador2.pack(fill="x", padx=15, pady=15)

    # -------------------------
    # TOTAL GRANDE
    # -------------------------
    lbl_total = tk.Label(
        frame_ticket,
        text=f"TOTAL: ${total}",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="#27AE60"
    )
    lbl_total.pack(pady=10)

    # -------------------------
    # MENSAJE FINAL
    # -------------------------
    lbl_gracias = tk.Label(
        frame_ticket,
        text="¡GRACIAS POR SU COMPRA!",
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#5C6AE9"
    )
    lbl_gracias.pack(pady=(10, 5))

    lbl_vuelva = tk.Label(
        frame_ticket,
        text="Vuelva pronto 😊",
        font=("Arial", 10),
        bg="white",
        fg="gray"
    )
    lbl_vuelva.pack()

    # -------------------------
    # BOTÓN CERRAR
    # -------------------------
    btn_cerrar = tk.Button(
        frame_ticket,
        text="Cerrar",
        font=("Arial", 11, "bold"),
        bg="#5C6AE9",
        fg="white",
        activebackground="#3F51D6",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=18,
        height=1,
        command=ticket.destroy
    )

    btn_cerrar.pack(pady=20)
def abrir_registro_ventas():
   ven = tk.Toplevel()
   ven.title("Registro de Ventas")
   ven.geometry("420x430")
   ven.resizable(False, False)
   # ------------------------------------
   # Cargar productos desde productos.txt
   # ------------------------------------
   productos = {}

   try:
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivof = os.path.join(BASE_DIR,"productos.txt")
      with open(archivof, "r", encoding="utf-8") as archivo:
         for linea in archivo:
            partes = linea.strip().split("|")
            if len(partes) == 4:
               idp, desc, precio, cat = partes
               productos[desc] = float(precio)
   except FileNotFoundError:
      messagebox.showerror("Error", "No se encontró el archivo productos.txt")
      ven.destroy()
      return
# Lista de nombres de productos
   lista_productos = list(productos.keys())
   # ------------------------------------
   # CONTROLES VISUALES
   # ------------------------------------
   lbl_prod = tk.Label(ven, text="Producto:", font=("Arial", 12))
   lbl_prod.pack(pady=5)
   cb_producto = ttk.Combobox(ven, values=lista_productos, font=("Arial", 12), state="readonly")
   cb_producto.pack(pady=5)
   lbl_precio = tk.Label(ven, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_precio.pack(pady=5)
   lbl_cantidad = tk.Label(ven, text="Cantidad:", font=("Arial", 12))
   lbl_cantidad.pack(pady=5)
   cantidad_var = tk.StringVar(ven)
   ven.cantidad_var = cantidad_var   # importante: mantiene la referencia
   txt_cantidad = tk.Entry(ven, font=("Arial", 12), textvariable=cantidad_var)
   txt_cantidad.pack(pady=5)  
   cantidad_var.trace_add("write", lambda *args: calcular_total())
   lbl_total = tk.Label(ven, text="Total:", font=("Arial", 12))
   lbl_total.pack(pady=5)
   txt_total = tk.Entry(ven, font=("Arial", 12), state="readonly")
   txt_total.pack(pady=5)

   # ------------------------------------
   # FUNCIONES
   # ------------------------------------
   def actualizar_precio(event):      
      prod = cb_producto.get()
      if prod in productos:
         txt_precio.config(state="normal")
         txt_precio.delete(0, tk.END)
         txt_precio.insert(0, productos[prod])
         txt_precio.config(state="readonly")
         calcular_total()

   def calcular_total(*args):      
      try:
         cant = int(txt_cantidad.get())
         precio = float(txt_precio.get())
         total = cant * precio
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.insert(0, total)
         txt_total.config(state="readonly")
      except:
         # Si no hay número válido, limpiar el total
         txt_total.config(state="normal")
         txt_total.delete(0, tk.END)
         txt_total.config(state="readonly")

   def registrar_venta():
      prod = cb_producto.get()
      precio = txt_precio.get()
      cant = txt_cantidad.get()
      total = txt_total.get()
      if prod == "" or precio == "" or cant == "" or total == "":
         messagebox.showwarning("Campos Vacíos", "Todos los campos deben estar completos.")
         return
      # Guardar venta
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivov = os.path.join(BASE_DIR,"ventas.txt")
      with open(archivov, "a", encoding="utf-8") as archivo:
         archivo.write(f"{prod}|{precio}|{cant}|{total}\n")
         messagebox.showinfo("Venta Registrada", "La venta se registró correctamente.")
         # --- MOSTRAR TICKET ---
         mostrar_ticket(prod, precio, cant, total)
      # Limpiar campos
      cb_producto.set("")
      txt_precio.config(state="normal"); txt_precio.delete(0, tk.END); txt_precio.config(state="readonly")
      txt_cantidad.delete(0, tk.END)
      txt_total.config(state="normal"); txt_total.delete(0, tk.END); txt_total.config(state="readonly")
   # ------------------------------------
   # EVENTOS Y BOTÓN
   # ------------------------------------
   cb_producto.bind("<<ComboboxSelected>>", actualizar_precio)
   btn_guardar = ttk.Button(ven, text="Registrar Venta", command=registrar_venta)
   btn_guardar.pack(pady=25)

        

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