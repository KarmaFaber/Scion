#python modules----------------------------------------------------
from tkinter import *
from tkinter import messagebox
import json
#my modules-------------------------------------------------------

#-----------------------------------------------------
def aniadir_mesa():
    root=Tk()
    root.title("añadir mesa")
    root.geometry("1400x500")
    root.config(bg="#FFC867")

    #myvariables------------------------
    
    master=StringVar()
    mesa=StringVar()
    #------------------
    jugador1=StringVar()
    jugador2=StringVar()
    jugador3=StringVar()
    jugador4=StringVar()
    jugador5=StringVar()
    #------------------
    personaje1=StringVar()
    personaje2=StringVar()
    personaje3=StringVar()
    personaje4=StringVar()
    personaje5=StringVar()
    #------------------
    vel_mov_pers1=StringVar()
    vel_mov_pers2=StringVar()
    vel_mov_pers3=StringVar()
    vel_mov_pers4=StringVar()
    vel_mov_pers5=StringVar()

    #--------------------
    
    nombre_pnj=StringVar()
    iniciativa_pnj=StringVar()
    
    

    #mylabels----------------------------
    lblJuego=Label(root, text="Juego: ", bg="#FFC867")
    lblJuego.config(font=("Courtier", 12))
    lblJuego.grid(row=3, column=2, padx=10, pady=10)

    lblJuego1=Label(root, text="Scion.", bg="#FFC867")
    lblJuego1.config(font=("Courtier", 12))
    lblJuego1.grid(row=3, column=3, padx=10, pady=10)

    #-------------------------------------
    lblMaster=Label(root, text="Nombre Master: ", bg="#FFC867")
    lblMaster.config(font=("Courtier", 12))
    lblMaster.grid(row=4, column=2, padx=10, pady=10)

    lblMesa=Label(root, text="Nombre Mesa: ", bg="#FFC867")
    lblMesa.config(font=("Courtier", 12))
    lblMesa.grid(row=5, column=2, padx=10, pady=10)

    #--------------------------------------
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

    #----------------------------------------
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

    #----------------------------------------------
    lblMov_Velocidad_jug1=Label(root, text="Velocidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad_jug1.config(font=("Courtier", 12))
    lblMov_Velocidad_jug1.grid(row=6, column=6, padx=10, pady=10)

    lblMov_Velocidad_jug2=Label(root, text="Velocidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad_jug2.config(font=("Courtier", 12))
    lblMov_Velocidad_jug2.grid(row=7, column=6, padx=10, pady=10)

    lblMov_Velocidad_jug3=Label(root, text="Velocidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad_jug3.config(font=("Courtier", 12))
    lblMov_Velocidad_jug3.grid(row=8, column=6, padx=10, pady=10)

    lblMov_Velocidad_jug4=Label(root, text="Velocidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad_jug4.config(font=("Courtier", 12))
    lblMov_Velocidad_jug4.grid(row=9, column=6, padx=10, pady=10)

    lblMov_Velocidad_jug5=Label(root, text="Velocidad de movimiento: ", bg="#FFC867")
    lblMov_Velocidad_jug5.config(font=("Courtier", 12))
    lblMov_Velocidad_jug5.grid(row=10, column=6, padx=10, pady=10)

#entry (input box)--------------------
    #-----------------------------------
    masterBox=Entry(root, bg="#F87C56", fg="#274017")
    masterBox.config(font=("Courtier", 12))
    masterBox.focus()
    masterBox.grid(row=4, column=3, padx=10, pady=10)

    mesaBox=Entry(root, bg="#F87C56", fg="#274017")
    mesaBox.config(font=("Courtier", 12))
    mesaBox.focus()
    mesaBox.grid(row=5, column=3, padx=10, pady=10)

    #--------------------------------------
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

    #------------------------------------------------
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


    #---------------------------------------------------
    vel_mov_pers1_box=Entry(root, bg="#F87C56", fg="#274017")
    vel_mov_pers1_box.config(font=("Courtier",12))
    vel_mov_pers1_box.focus()
    vel_mov_pers1_box.grid(row=6, column=7, padx=10, pady=10)

    vel_mov_pers2_box=Entry(root, bg="#F87C56", fg="#274017")
    vel_mov_pers2_box.config(font=("Courtier",12))
    vel_mov_pers2_box.focus()
    vel_mov_pers2_box.grid(row=7, column=7, padx=10, pady=10)

    vel_mov_pers3_box=Entry(root, bg="#F87C56", fg="#274017")
    vel_mov_pers3_box.config(font=("Courtier",12))
    vel_mov_pers3_box.focus()
    vel_mov_pers3_box.grid(row=8, column=7, padx=10, pady=10)

    vel_mov_pers4_box=Entry(root, bg="#F87C56", fg="#274017")
    vel_mov_pers4_box.config(font=("Courtier",12))
    vel_mov_pers4_box.focus()
    vel_mov_pers4_box.grid(row=9, column=7, padx=10, pady=10)

    vel_mov_pers5_box=Entry(root, bg="#F87C56", fg="#274017")
    vel_mov_pers5_box.config(font=("Courtier",12))
    vel_mov_pers5_box.focus()
    vel_mov_pers5_box.grid(row=10, column=7, padx=10, pady=10)
  


    #---------------------------------------------------
    def guardar_datos_mesa(): #nueva mesa
        #---------variables - get text box--------------
        master=masterBox.get()
        mesa=mesaBox.get()

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

        vel_mov_pers1=vel_mov_pers1_box.get()
        vel_mov_pers2=vel_mov_pers2_box.get()
        vel_mov_pers3=vel_mov_pers3_box.get()
        vel_mov_pers4=vel_mov_pers4_box.get()
        vel_mov_pers5=vel_mov_pers5_box.get()


        
        #Convertimos los string de master y mesa en nombre de Json
        mesa=str(mesa)
        master=str(master)
        nombre_mesa=(master +"_"+ mesa)

        #comprobar el formato de la selda antes de la escritura
        if len(master)and len(mesa) and len(jugador1) and len(jugador2) and len(jugador3) and len(jugador4) and len(jugador5) and len(personaje1) and len(personaje2) and len(personaje3) and len(personaje4) and len(personaje5)and len(vel_mov_pers1) and len(vel_mov_pers2) and len(vel_mov_pers3) and len(vel_mov_pers4) and len(vel_mov_pers5)!=0:
        #json ------------------------------------------------------
            nombre_mesa={
            nombre_mesa:[
            {'datos jugador1':[{'Nombre jugador 1:': jugador1, 'Personaje 1: ': personaje1, 'Volocidad de movimiento personaje 1: ': vel_mov_pers1 }]},
            {'datos jugador2':[{'Nombre jugador 2:': jugador2, 'Personaje 2: ': personaje2, 'Volocidad de movimiento personaje 2: ': vel_mov_pers2 }]},
            {'datos jugador3':[{'Nombre jugador 3:': jugador3, 'Personaje 3: ': personaje3, 'Volocidad de movimiento personaje 3: ': vel_mov_pers3 }]},
            {'datos jugador4':[{'Nombre jugador 4:': jugador4, 'Personaje 4: ': personaje4, 'Volocidad de movimiento personaje 4: ': vel_mov_pers4 }]},
            {'datos jugador5':[{'Nombre jugador 5:': jugador5, 'Personaje 5: ': personaje5, 'Volocidad de movimiento personaje 5: ': vel_mov_pers5 }]}
            
                        ]
                        }
                        
            mesa_json =json.dumps(nombre_mesa)
 #           print(mesa_json)  
            root.destroy()
        
        else:
            messagebox.showinfo(message="Algúno de los campos esta en vacio", title="Creación de nueva mesa")
            root.destroy()



    def limpiar(): #limpiar los campos del formulafio jugador Box's
        
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

        vel_mov_pers1_box.delete(0, END)
        vel_mov_pers2_box.delete(0, END)
        vel_mov_pers3_box.delete(0, END)
        vel_mov_pers4_box.delete(0, END)
        vel_mov_pers5_box.delete(0, END)


    def aniadir_jugador():
        pass
    def modificar_datos_mesa():
        pass

    

    #BOTONES ROOT NUEVA_MESA:--------------------------------
    btn_guardar_mesa=Button(root, text="Guardar datos de la mesa", command=guardar_datos_mesa, bg="#FAF3E3")
    btn_guardar_mesa.config(font=("Courtier", 12))
    btn_guardar_mesa.grid(row=11, column=2, padx=20, pady=20)

    btn_modificar_mesa=Button(root, text="Modificar datos de la mesa", command=modificar_datos_mesa, bg="#FAF3E3")
    btn_modificar_mesa.config(font=("Courtier", 12))
    btn_modificar_mesa.grid(row=11, column=3, padx=20, pady=20)

    btn_limpiar=Button(root, text="Limpiar todas las casillas", command=limpiar, bg="#FAF3E3")
    btn_limpiar.config(font=("Courtier", 12))
    btn_limpiar.grid(row=11, column=4, padx=20, pady=20)

    btn_otro_pers=Button(root, text="Añadir otro jugador", command=aniadir_jugador, bg="#FAF3E3")
    btn_otro_pers.config(font=("Courtier", 12))
    btn_otro_pers.grid(row=11, column=5, padx=20, pady=20)


    #fin root-------------------------------------------------------
    root.mainloop()



