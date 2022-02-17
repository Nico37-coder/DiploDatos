from tkinter import*
from tkinter import ttk


class view():

    def __init__(self,window):

        self.root=window


        self.root.title("Tarea Patrón Observador")
        self.root["bg"] = "medium spring green"
        self.root.geometry("1250x450")
        self.root.resizable(True,True)
       # self.root.iconbitmap("pythonlogo.ico")
        #Contenedor
        self.miFrame = Frame(self.root)
        self.miFrame.pack()
        self.miFrame.config(pady=5,bg="medium spring green")
        #Defino variables globales:
        self.titulo_var=StringVar()
        self.descripcion_var=StringVar()
        self.tema_var = IntVar(value=0)
        self.var_color = "medium spring green"
        #Secciones
        self.sec_sup=Frame(self.miFrame)
        self.sec_sup.pack()
        self.sec_sup.config(bg=self.var_color)
        self.sec_int=Frame(self.miFrame)
        self.sec_int.pack()
        self.sec_int.config(bg=self.var_color)
        self.sec_inf=Frame(self.miFrame)
        self.sec_inf.pack()
        self.sec_inf.config(bg=self.var_color)

#________________________________Seccion Superior___________________________________________

        #Label Titulo:
        self.label_titulo=Label(self.sec_sup, text="Ingrese sus datos",bg="medium spring green",fg="white",font=("Segoe",13,"bold"),width=60 )
        self.label_titulo.grid(row=0,columnspan=15,sticky=W+E)

        #Entries
        self.sec_sup.e_titulo= Entry(self.sec_sup, width = 70,textvariable=self.titulo_var)
        self.sec_sup.e_titulo.focus_set()
        self.sec_sup.e_descripcion= Entry (self.sec_sup, width = 70,textvariable=self.descripcion_var)
        self.sec_sup.e_titulo.grid(row=2, column=2,columnspan=5)
        self.sec_sup.e_descripcion.grid(row=4, column=2,columnspan=5)
        #Label/Grid:
        self.label1=Label(self.sec_sup,text="Título:",font=("Segoe"),bg="medium spring green",fg="black")
        self.label1.grid(row=2,column=0,sticky=W)
        self.label2=Label(self.sec_sup, text="Descripción:",font=("Segoe"),bg="medium spring green",fg="black" )
        self.label2.grid(row=4,column=0,sticky=W)
        #Boton cerrar
        #self.boton_cerrar = Button(self.sec_sup, text="Cerrar", font=("Segoe",7,"bold"),bg="grey73", fg="black")
        #self.boton_cerrar.place(x=555, y=3, width=40, height=20)

#____________________________________Seccion Intermedia______________________________________

#---------------------------------------TREEVIEW-----------------------------------

        # Fifth row - Treeview
        self.tree= ttk.Treeview(self.sec_int, columns=("size", "lastmod"))
        self.tree.grid(row=6, columnspan=4, sticky="nsew")
        # Adding headings
        self.tree["columns"] = ("1", "2", "3","4","5","6")
        self.tree['show'] = 'headings'
        self.tree.heading("1", text="Id")
        self.tree.heading("2", text="Titulo")
        self.tree.heading("3", text="Descripción")
        self.tree.heading("4", text="Fecha")
        self.tree.heading("5", text="Estado")
        self.tree.heading("6", text="Objeto")
        # Adding scrollbar to treeview
        Scrollbar_vertical = ttk.Scrollbar(self.sec_int, orient='vertical', command=self.tree.yview)
        Scrollbar_vertical.grid(row=6, column=4, sticky="nsew")
        self.tree.configure(yscrollcommand=Scrollbar_vertical.set)

#---------------------------------------BUTTONS--------------------------------------

        self.boton_alta=Button(self.sec_int, text="Alta",bg="grey93",fg="black",padx ="15",font=("Helvetica",8,"bold"))
        self.boton_alta.grid(padx=10,row=4,column=0)

        self.boton_eliminar=Button(self.sec_int, text="Eliminar",bg="grey93",fg="black",padx ="10",font=("Helvetica",8,"bold"))
        self.boton_eliminar.grid(padx=10,row=4,column=3)

        self.boton_modifica=Button(self.sec_int, text="Actualizar",bg="grey93",fg="black",padx ="10",font=("Helvetica",8,"bold"))
        self.boton_modifica.grid(padx=360,row=4,column=1)

        self.boton_pdf = Button(self.sec_int, text="PDF",bg="red",fg="white",padx ="10",font=("Helvetica",8,"bold"))
        self.boton_pdf.grid(padx=10,row=14,column=0)

        #self.boton_excel = Button(self.sec_int, text="XLS",bg="green",fg="white",padx ="10",font=("Helvetica",8,"bold"))
        #self.boton_excel.grid(padx=10,row=14,column=3)

        self.boton_fake = Button(self.sec_int, text="Fake x1",bg="blue",fg="white",font=("Helvetica",8,"bold"))
        self.boton_fake.grid(row=14, ipadx=12, padx=5, column=1, sticky=E)

#____________________________________Sección Inferior___________________________________

        self.radio_white = Radiobutton(self.sec_inf,borderwidth=2, text="Tema 1",
                    bg="medium spring green", fg="black", width=10, variable=self.tema_var,font=("Segoe",7,"bold"),
                    value=0)
        self.radio_white.pack(side=LEFT)
        self.radio_black = Radiobutton(self.sec_inf, borderwidth=2,text="Tema 2",
                    bg="medium spring green", fg="black", width=10, variable=self.tema_var,font=("Segoe",7,"bold"),
                    value=1)
        self.radio_black.pack(side=LEFT)
        self.radio_random = Radiobutton(self.sec_inf,borderwidth=2, text="Random",
                    bg="medium spring green", fg="black", width=10, variable=self.tema_var,font=("Segoe",7,"bold"),
                    value=2)
        self.radio_random.pack(side=LEFT)








