 
import tkinter as tk
from tkinter import font

# Crear ventana
ventana = tk.Tk()
ventana.title("Programa para subir a repositorio")
ventana.geometry("500x300")  # un poco más grande para que el texto destaque
ventana.configure(bg="#75B8C5")  # fondo oscuro elegante

# Crear un estilo de fuente grande y llamativo
fuente_personalizada = font.Font(family="Comic Sans MS", size=18, weight="bold", slant="italic")

# Crear etiqueta con colores y fuente personalizada
etiqueta = tk.Label(
    ventana,
    text="¡Este Programa Es De Irvin y Cesar!",
    font=fuente_personalizada,
    fg="#309cc7",  # color rosa brillante
    bg="#fdfcfc"   # mismo color de fondo que la ventana
)
etiqueta.pack(pady=40)

# Mostrar ventana
ventana.mainloop()
