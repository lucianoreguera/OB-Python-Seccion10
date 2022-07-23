from tkinter import *


root = Tk()

elemento = StringVar()

listbox = Listbox(root)

paises = ["Argentina", "España", "Italia", "Uruguay", "Alemania", "Noruega", "Suecia", "Finlandia"]

for pais in paises:
    listbox.insert(END, pais)

listbox.pack()

label = Label(text="Listado de Países")
label.pack()

root.mainloop()
