#python modules----------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pymysql
import pymysql.cursors

#my modules-------------------------------------------------------
from myRoots.iniciativa import iniciativa
from myRoots.mesa_nueva import aniadir_mesa
from myRoots.modificar_mesa import modificar_mesa


#variables globañes----------------------------
global contrasenia_log
global master_log
#----------------------------------------------------------------------------------------------------------------------------------------



#tkinter: Scion main root-----------------------------------------------------------------------------------------------------------------
root=Tk()
root.title("Scion Log In")

root.geometry("600x400")
root.config(bg="#FFC867")

#myvariables------------------------
    
master_log=StringVar()
contrasenia_log=StringVar()


#label and entry box login------------
lbl_master=Label(root, text="Nombre del master: ", bg="#ffc867")
lbl_master.config(font=("Courtier", 12))
lbl_master.grid(row=2, column=2, padx=10, pady=10)

lbl_contrasenia=Label(root, text="Contraseña: ", bg="#ffc867")
lbl_contrasenia.config(font=("Courtier", 12))
lbl_contrasenia.grid(row=3, column=2, padx=10, pady=10)


box_master=Entry(root, bg="#F87C56", fg="#274017")
box_master.config(font=("Courtier",12))
box_master.focus()
box_master.grid(row=2, column=3, padx=10, pady=10)

box_contrasenia=Entry(root, bg="#F87C56", fg="#274017")
box_contrasenia.config(font=("Courtier",12))
box_contrasenia.focus()
box_contrasenia.grid(row=3, column=3, padx=10, pady=10)



#--------------------exportar def index a otra parte luego-----------------------------------
def index():
    #variables---------------------------
    master_log=box_master.get()
    contrasenia_log=box_contrasenia.get()
    

    #mysql----------------------------
    try:
        #sql query:------------
        db=pymysql.connect("localhost", "root", "", "scion")
        cursor=db.cursor()
        query="select * from master where NOMBRE_MASTER='%s'"%master_log
        cursor.execute(query)
        

        result=cursor.fetchall()
        for row in result:
            nombre_master=row[1]
            contrasenia=row[2]
            ("NOMBRE_MASTER={1}, contrasenia{2}".format(nombre_master, contrasenia))
        
            
        
        if contrasenia_log==contrasenia:
            #tkinter: Scion secondary root------------------------------------------------------------------------------------------------------------------------------------------------
            root=Tk()
            root.title("Scion interface: Index.")

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

            #fin root index------------------------------------------
            root.mainloop()

        else:
            messagebox.showerror(message="los datos son incorrectos", title="Log In message :)")
            box_master.delete(0,END)
            box_contrasenia.delete(0,END)

    

    except TypeError:
        messagebox.showwarning(message="some kind of format error is found: please type your password again", title="Warning")
        box_contrasenia.delete(0,END)
    except OperationalError: 
        messagebox.showwarning(message="A connection cannot be established since the destination team expressly denies that connection.", title="Warning")
    except ConnectionRefusedError:
        messagebox.showwarning(message="Error connecting to the database, check your connection to the server and try again.", title="Warning")
    except InternalError:
        messagebox.showwarning(message="Check the connection data to the BD.", title="Warning")
    except UnboundLocalError: 
        messagebox.showwarning(message="email not found.", title="Warning")

#buttons--------------------------------------------------------------
btn_login=Button(root, text="Entrar Index", command=index, bg="#FAA3E3")
btn_login.config(font=("Courtier", 12))
btn_login.grid(row=5, column=2, padx=20, pady=20)
    

#fin root index------------------------------------------
root.mainloop()