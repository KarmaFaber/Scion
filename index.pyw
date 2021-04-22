#python modules----------------------------------------------------
from tkinter import *
from tkinter import messagebox
#my modules-------------------------------------------------------



#tkinter root-------------------------------------------------------
root=Tk()
root.title("Scion interface")
root.geometry("400x400")
root.config(bg="#FFC867")

#defs--------------------------------------
def aniadir_mesa():
    root=Tk()
    root.title("añadir mesa")
    root.geometry("800x500")
    root.config(bg="#FFC867")

    #myvariables------------------------
    
    master=StringVar()
    mesa=StringVar()
    jugador1=StringVar()
    jugador2=StringVar()
    jugador3=StringVar()
    jugador4=StringVar()
    jugador5=StringVar()
    personaje1=StringVar()
    personaje2=StringVar()
    personaje3=StringVar()
    personaje4=StringVar()
    personaje5=StringVar()
    vel_movimiento=StringVar()
    nombre_pnj=StringVar()
    iniciativa_pnj=StringVar()
    
    

    #mylabels----------------------------
    lblJuego=Label(root, text="Juego: ", bg="#FFC867")
    lblJuego.config(font=("Courtier", 12))
    lblJuego.grid(row=3, column=2, padx=10, pady=10)

    lblJuego1=Label(root, text="Scion.", bg="#FFC867")
    lblJuego1.config(font=("Courtier", 12))
    lblJuego1.grid(row=3, column=3, padx=10, pady=10)

    lblMaster=Label(root, text="Nombre Master: ", bg="#FFC867")
    lblMaster.config(font=("Courtier", 12))
    lblMaster.grid(row=4, column=2, padx=10, pady=10)

    lblMesa=Label(root, text="Nombre Mesa: ", bg="#FFC867")
    lblMesa.config(font=("Courtier", 12))
    lblMesa.grid(row=5, column=2, padx=10, pady=10)

    lblJugador1=Label(root, text="jugador 1: ", bg="#FFC867")
    lblJugador1.config(font=("Courtier", 12))
    lblJugador1.grid(row=6, column=2, padx=10, pady=10)

    lblJugador2=Label(root, text="jugador 2:", bg="#FFC867")
    lblJugador2.config(font=("Courtier", 12))
    lblJugador2.grid(row=7, column=2, padx=10, pady=10)

    lblJugador3=Label(root, text="jugador 3: ", bg="#FFC867")
    lblJugador3.config(font=("Courtier", 12))
    lblJugador3.grid(row=8, column=2, padx=10, pady=10)

    lblJugador4=Label(root, text="jugador 4: ", bg="#FFC867")
    lblJugador4.config(font=("Courtier", 12))
    lblJugador4.grid(row=9, column=2, padx=10, pady=10)

    lblJugador5=Label(root, text="jugador 5: ", bg="#FFC867")
    lblJugador5.config(font=("Courtier", 12))
    lblJugador5.grid(row=10, column=2, padx=10, pady=10)

    lblPersonaje1=Label(root, text="Personaje 1: ", bg="#FFC867")
    lblPersonaje1.config(font=("Courtier", 12))
    lblPersonaje1.grid(row=6, column=4, padx=10, pady=10)

    lblPersonaje2=Label(root, text="Personaje 2:", bg="#FFC867")
    lblPersonaje2.config(font=("Courtier", 12))
    lblPersonaje2.grid(row=7, column=4, padx=10, pady=10)

    lblPersonaje3=Label(root, text="Personaje 3: ", bg="#FFC867")
    lblPersonaje3.config(font=("Courtier", 12))
    lblPersonaje3.grid(row=8, column=4, padx=10, pady=10)

    lblPersonaje4=Label(root, text="Personaje 4: ", bg="#FFC867")
    lblPersonaje4.config(font=("Courtier", 12))
    lblPersonaje4.grid(row=9, column=4, padx=10, pady=10)

    lblPersonaje5=Label(root, text="Personaje 5: ", bg="#FFC867")
    lblPersonaje5.config(font=("Courtier", 12))
    lblPersonaje5.grid(row=10, column=4, padx=10, pady=10)


    lblMov_Velocidad=Label(root, text="Velovidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad.config(font=("Courtier", 12))
    lblMov_Velocidad.grid(row=11, column=4, padx=10, pady=10)

    #entry (input box)--------------------

    masterBox=Entry(root, bg="#F87C56", fg="#274017")
    masterBox.config(font=("Courtier", 12))
    masterBox.focus()
    masterBox.grid(row=4, column=3, padx=10, pady=10)

    mesaBox=Entry(root, bg="#F87C56", fg="#274017")
    mesaBox.config(font=("Courtier", 12))
    mesaBox.focus()
    mesaBox.grid(row=5, column=3, padx=10, pady=10)

    jugador1Box=Entry(root, bg="#F87C56", fg="#274017")
    jugador1Box.config(font=("Courtier", 12))
    jugador1Box.focus()
    jugador1Box.grid(row=6, column=3, padx=10, pady=10)

    jugador2Box=Entry(root, bg="#F87C56", fg="#274017")
    jugador2Box.config(font=("Courtier", 12))
    jugador2Box.focus()
    jugador2Box.grid(row=7, column=3, padx=10, pady=10)

    jugador3Box=Entry(root, bg="#F87C56", fg="#274017")
    jugador3Box.config(font=("Courtier", 12))
    jugador3Box.focus()
    jugador3Box.grid(row=8, column=3, padx=10, pady=10)

    jugador4Box=Entry(root, bg="#F87C56", fg="#274017")
    jugador4Box.config(font=("Courtier", 12))
    jugador4Box.focus()
    jugador4Box.grid(row=9, column=3, padx=10, pady=10)

    jugador5Box=Entry(root, bg="#F87C56", fg="#274017")
    jugador5Box.config(font=("Courtier", 12))
    jugador5Box.focus()
    jugador5Box.grid(row=10, column=3, padx=10, pady=10)


    personaje1Box=Entry(root, bg="#F87C56", fg="#274017")
    personaje1Box.config(font=("Courtier", 12))
    personaje1Box.focus()
    personaje1Box.grid(row=6, column=5, padx=10, pady=10)

    personaje2Box=Entry(root, bg="#F87C56", fg="#274017")
    personaje2Box.config(font=("Courtier", 12))
    personaje2Box.focus()
    personaje2Box.grid(row=7, column=5, padx=10, pady=10)

    personaje3Box=Entry(root, bg="#F87C56", fg="#274017")
    personaje3Box.config(font=("Courtier", 12))
    personaje3Box.focus()
    personaje3Box.grid(row=8, column=5, padx=10, pady=10)

    personaje4Box=Entry(root, bg="#F87C56", fg="#274017")
    personaje4Box.config(font=("Courtier", 12))
    personaje4Box.focus()
    personaje4Box.grid(row=9, column=5, padx=10, pady=10)

    personaje5Box=Entry(root, bg="#F87C56", fg="#274017")
    personaje5Box.config(font=("Courtier", 12))
    personaje5Box.focus()
    personaje5Box.grid(row=10, column=5, padx=10, pady=10)


    #tiene que ser velocidad de movimiento de cada personaje x5
    vel_movimiento=Entry(root, bg="#F87C56", fg="#274017")
    vel_movimiento.config(font=("Courtier",12))
    vel_movimiento.focus()
    vel_movimiento.grid(row=11, column=5, padx=10, pady=10)



    def guardar_datos_mesa(): #nueva mesa
        master=masterBox.get()
        mesa=mesaBox.get()
        vel_movimiento.get()

        jugador1=jugador1Box.get()
        jugador2=jugador2Box.get()
        jugador3=jugador3Box.get()
        jugador4=jugador4Box.get()
        jugador5=jugador5Box.get()

        personaje1=personaje1Box.get()
        personaje2=personaje2Box.get()
        personaje3=personaje3Box.get()
        personaje4=personaje4Box.get()
        personaje5=personaje5Box.get()


        #añadir la velocidad de movimiento a la escrituda de datos
        if len(master)and len(mesa) and len(jugador1) and len(jugador2) and len(jugador3) and len(jugador4) and len(jugador5) and len(personaje1) and len(personaje2) and len(personaje3) and len(personaje4) and len(personaje5)and len(vel_movimiento)!=0:
            creaccion_de_mesa_nueva={"master": master, "mesa":mesa, "jugador 1":jugador1, "personaje 1":personaje1, "jugador 2": jugador2, "personaje 2": personaje2, "jugador 3": jugador3, "personaje 3": personaje3, "jugador 4": jugador4, "personaje 4": personaje4, "jugador 5": jugador5, "personaje 5": personaje5, "velocidad_movimiento":vel_movimiento}
            f=open('C:/Users/Usuario/Desktop/Scion/%s_%s.txt'%(mesa, master), 'a')
            texto=str(creaccion_de_mesa_nueva)
            f.write(texto)
            f.close()
            root.destroy()
        else:
            messagebox.showinfo(message="Algúno de los campos esta en vacio", title="Creación de nueva mesa")

    def limpiar(): #limpiar los campos del formulafio jugador Box's
        #añadir limpiar los campos de velocidad de movimiento en la limpieza
        jugador1Box.delete(0, END)
        jugador2Box.delete(0, END)
        jugador3Box.delete(0, END)
        jugador4Box.delete(0, END)
        jugador5Box.delete(0, END)

        personaje1Box.delete(0, END)
        personaje2Box.delete(0, END)
        personaje3Box.delete(0, END)
        personaje4Box.delete(0, END)
        personaje5Box.delete(0, END)

    btn_guardar_mesa=Button(root, text="guardar datos", command=guardar_datos_mesa, bg="#FAF3E3")
    btn_guardar_mesa.config(font=("Courtier", 12))
    btn_guardar_mesa.grid(row=11, column=2, padx=20, pady=20)

    btn_limpiar=Button(root, text="limpiar", command=limpiar, bg="#FAF3E3")
    btn_limpiar.config(font=("Courtier", 12))
    btn_limpiar.grid(row=11, column=3, padx=20, pady=20)
    root.mainloop()

def iniciativa():
    root=Tk()
    root.title("iniciativas")
    root.geometry("600x500")
    root.config(bg="#FFC867")
    
    def aniadir_pnjs():
        nombre_pnj=nombre_pnjs_box.get()
        iniciativa_pnj=nombre_pnjs_box.get()

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

#buttns--------------------------------------------------------------

btn_aniadir_datos=Button(root, text="añadir mesa", command=aniadir_mesa, bg="#FAF3E3")
btn_aniadir_datos.config(font=("Courtier", 12))
btn_aniadir_datos.grid(row=5, column=2, padx=20, pady=20)

btn_iniciativa=Button(root, text="Iniciativas", command=iniciativa, bg="#FAF3E3")
btn_iniciativa.config(font=("Courtier", 12))
btn_iniciativa.grid(row=9, column=2, padx=20, pady=20)

root.mainloop()