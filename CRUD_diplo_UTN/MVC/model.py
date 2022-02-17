from tkinter.messagebox import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from modulo_validacion.validacion import*
from peewee import *
import datetime, os
from faker import Faker
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from Observador import*


#Decoradores
def funcion_log(log_mensaje):
    log_instante=str(datetime.datetime.now())
    log_registro=log_instante+ "-" +log_mensaje+"\n"
   # print(log_registro)
    with open("log.txt", "a+") as archivo:
        archivo.write(log_registro)

def decorador_alta(funcion):
    def funcion_envoltura(*args):
        datos=funcion(*args)
        log_mensaje="Alta de registro"
        funcion_log(log_mensaje)
    return funcion_envoltura


def decorador_eliminar(funcion):
    def funcion_envoltura(*args):
        datos=funcion(*args)
        log_mensaje="Registro eliminado"
        funcion_log(log_mensaje)
    return funcion_envoltura

def decorador_actualizar(funcion):
    def funcion_envoltura(*args):
        datos=funcion(*args)
        log_mensaje="Registro actualizado"
        funcion_log(log_mensaje)
    return funcion_envoltura

def decorador_fake(funcion):
    def funcion_envoltura(*args):
        datos=funcion(*args)
        log_mensaje="Registro creado aleatoriamente"
        funcion_log(log_mensaje)
    return funcion_envoltura

#### CREAR BASE DE DATOS CON PEEWEE ####

db = SqliteDatabase('DataBasePeewee2.db')

class BaseModel(Model):
    titulo = CharField()
    descripcion = TextField()
    fecha = DateTimeField(default=datetime.datetime.now)
    estado_de_publicacion = BooleanField(default=True)
    class Meta:
        database = db
    def __str__(self):
        objeto="El titulo es "
        return objeto + self.titulo

BaseModel.create_table()

class model(TemaConcreto):


    def limpiar(self,titulo_var, descripcion_var):
            titulo_var.set("")
            descripcion_var.set("")

    @decorador_alta
    def ingresodatos(self,titulo_var, descripcion_var):
        if validar(titulo_var)== "True":
            question1 = messagebox.askquestion("Alta", "¿Desea dar el ALTA el registro: \n {} {}?".format
                                                         (titulo_var.get(),
                                                          descripcion_var.get()))
            if question1 =="yes":
                alta = BaseModel()#creo un objeto de la clase BaseModel
                alta.titulo = titulo_var.get()
                alta.descripcion = descripcion_var.get()
                alta.objeto = "El titulo es: " + str(alta)
                alta.save()
                messagebox.showinfo("BBDD","Registro incertado con exito")

                observador = ConcreteObserverAlta(self)#Vinculado a Patron Observador
                estado = True#Vinculado a Patron Observador
                self.SetEstado(estado)#Vinculado a Patron Observador
                self.limpiar(titulo_var,descripcion_var)
            else:
                self.limpiar(titulo_var,descripcion_var)
        else:
            self.limpiar(titulo_var,descripcion_var)


    def consultar(self,tree):
        try:
            # Limpiando TreeView#
            registros=tree.get_children()
            for i in registros:
                tree.delete(i)
            # Consultando tabla
            for dato in BaseModel.select():
                tree.insert('', 0, values = (dato.id, dato.titulo,dato.descripcion,dato.fecha,dato.estado_de_publicacion,dato))
        except:
            messagebox.showerror("Error",
            "Problemas al consultar base de datos")

    @decorador_actualizar
    def actualizar(self, seleccion, titulo_var, descripcion_var):
        try:
            if not seleccion["values"]:
                messagebox.showerror("Error de seleccion",
                "Seleccione una linea por favor")
                return
            if validar(titulo_var)== "False":
                self.limpiar(titulo_var,descripcion_var)
                return
            actualizar=BaseModel.update(titulo=titulo_var.get(),
                       descripcion = descripcion_var.get()).where(BaseModel.id == seleccion["values"][0])

            actualizar.execute()
            observador = ConcreteObserverModifica(self)#Vinculado a Patron Observador
            estado = True #Vinculado a Patron Observador
            self.SetEstado(estado)#Vinculado a Patron Observador
            self.limpiar(titulo_var,descripcion_var)
        except:
            messagebox.showerror("Error",
            "Compruebe su conexión a la base de datos")
            self.limpiar(titulo_var,descripcion_var)

    @decorador_eliminar
    def eliminar(self,seleccion):
        try:
            if not seleccion["values"]:
                messagebox.showerror("Error de seleccion",
                "Seleccione una linea por favor")
                return
            eliminar=BaseModel.get(BaseModel.id==seleccion["values"][0])                                                     # descripcion_var.get()))
            eliminar.delete_instance()
            observador = ConcreteObserverBaja(self)#Vinculado a Patron Observador
            estado = False #Vinculado a Patron Observador
            self.SetEstado(estado) #Vinculado a Patron Observador

        except:
            messagebox.showerror("Error",
            "Compruebe su conexión a la base de datos")


    def generar_pdf(self,):
        try:
            styles = getSampleStyleSheet()
            report_title = Paragraph("Lista de registros", styles["h1"])
            report = SimpleDocTemplate("Reporte.pdf")

            table_data = []
            for a in BaseModel.select():
                table_data.append([a.id, a.titulo, a.descripcion, a.fecha, a.estado_de_publicacion])

            table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
            report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
            report.build([report_title, report_table])
            messagebox.showinfo("Informacion", "PDF generado con éxito, chequee en su directorio")
        except:
            messagebox.showerror("Error",
            "Problemas con ReportLab")


    @decorador_fake
    def fake(self,):
        try:
            fakegen = Faker()
            for entry in range(1):
                faketit = fakegen.first_name()
                fakedes = fakegen.job()
                fakeobj="El título es: " + str(faketit)
                falso = BaseModel()
                falso.titulo = faketit
                falso.descripcion = fakedes
                falso.objeto=fakeobj
                falso.save()
                observador = ConcreteObserverFake(self)#Vinculado a Patron Observador
                estado = True#Vinculado a Patron Observador
                self.SetEstado(estado)#Vinculado a Patron Observador
        except:
            messagebox.showerror("Error",
            "Algo salio mal con Faker")


    def abrir_fichero(self,):
        fichero=filedialog.askopenfilename(title="Abrir",initialdir="C:")
        print(fichero)


    def en_proceso(self,):
        print( "Paciencia...en proceso!")


