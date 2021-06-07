
#python modules----------------------------------------------------
from tkinter import *
from tkinter import messagebox
#my modules-------------------------------------------------------


#--root: iniciativa----------------------------------------------
def iniciativa():
    root=Tk()
    root.title("iniciativas")
    root.geometry("600x500")
    root.config(bg="#FFC867")
    
    def aniadir_pnjs():
        nombre_pnj=nombre_pnjs_box.get()
        iniciativa_pnj=iniciativa_box.get()

        if type(iniciativa_pnj)!=int:
            messagebox.showinfo(message="la iniciativa tiene que ser un numero", title="Iniciativas")
            root.destroy()
        else:
            print(nombre_pnj, iniciativa_pnj)
            root.destroy()

    
    lbl_nombre_pnj=Label(root, text="Nombre del PNJ: ", bg="#FFC867")
    lbl_nombre_pnj.config(font=("Courtier", 12)) 
    lbl_nombre_pnj.grid(row=2, column=2, padx=10, pady=10)

    nombre_pnjs_box=Entry(root, bg="#F87C56", fg="#274017")
    nombre_pnjs_box.config(font=("Courtier",12))
    nombre_pnjs_box.focus()
    nombre_pnjs_box.grid(row=2, column=3, padx=10, pady=10)

    lbl_iniciativa=Label(root, text="Iniciativa: ", bg="#FFC867")
    lbl_iniciativa.config(font=("Courtier", 12))
    lbl_iniciativa.grid(row=3, column=2, padx=10, pady=10)

    iniciativa_box=Entry(root, bg="#F87C56", fg="#274017")
    iniciativa_box.config(font=("Courtier",12))
    iniciativa_box.focus()
    iniciativa_box.grid(row=3, column=3, padx=10, pady=10)


    btn_aniadir_pnjts=Button(root, text="Añadir PNJ's", command=aniadir_pnjs, bg="#FAA3E3")
    btn_aniadir_pnjts.config(font=("Courtier", 12))
    btn_aniadir_pnjts.grid(row=4, column=2, padx=20, pady=20)


    root.mainloop()