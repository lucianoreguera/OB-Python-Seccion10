from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Samsung", variable=opcion, 
            value='Samsung', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Motorola", variable=opcion, 
            value='Motorola', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="LG", variable=opcion,   
            value='LG', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Huawei", variable=opcion,   
            value='Huawei', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="IPhone", variable=opcion,   
            value='IPhone', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()
