import leer
import tkinter as tk
import tkinter.filedialog


def cargar_archivo():
    ruta_archivo = tkinter.filedialog.askopenfilename()
    leer.Vetana(ruta_archivo)

root = tk.Tk()
root.geometry("300x100")

root.title('Buscador De Archivos')

label = tk.Label(root, text="Selecciona Un Archivo")
label.pack()


boton = tk.Button(root, text='Cargar archivo', command=cargar_archivo)
boton.pack()

root.mainloop()