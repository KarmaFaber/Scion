#python modules----------------------------------------------------
from tkinter import *
from tkinter import messagebox
#my modules-------------------------------------------------------
from myRoots.iniciativa import iniciativa
from myRoots.mesa_nueva import aniadir_mesa
from myRoots.modificar_mesa import modificar_mesa
#----------------------------------------------------------------


#tkinter: Scion main root------------------------------------------------------------------------------------------------------------------------------------------------
root=Tk()
root.title("Scion interface")

root.geometry("600x400")
root.config(bg="#FFC867")

#buttons--------------------------------------------------------------

btn_aniadir_datos=Button(root, text="Añadir mesa nueva", command=aniadir_mesa, bg="#FAF3E3")
btn_aniadir_datos.config(font=("Courtier", 12))
btn_aniadir_datos.grid(row=5, column=2, padx=20, pady=20)

btn_aniadir_datos=Button(root, text="Modificar datos de una mesa existente", command=modificar_mesa, bg="#FAF3E3")
btn_aniadir_datos.config(font=("Courtier", 12))
btn_aniadir_datos.grid(row=5, column=4, padx=20, pady=20)

btn_iniciativa=Button(root, text="Iniciativas", command=iniciativa, bg="#FAF3E3")
btn_iniciativa.config(font=("Courtier", 12))
btn_iniciativa.grid(row=9, column=2, padx=20, pady=20)

root.mainloop()