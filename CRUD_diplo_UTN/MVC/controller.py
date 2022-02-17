from tkinter import *
from tkinter import ttk
from model import*
from view import*
from modulo_temas.temas import*



class Controller():

    def __init__(self,window):

        self.root=window
        self.vista=view(self.root)
        self.modelo=model()

#--------------------Asocio botones de view con model---------------

        self.vista.boton_alta.config(command=self.altaDatos)
        self.consultaDatos()
        self.vista.boton_modifica.config(command=self.modificar)
        self.vista.boton_eliminar.config(command=self.baja)
        self.vista.radio_white.config(command=self.cambiarcolor)
        self.vista.radio_black.config(command=self.cambiarcolor)
        self.vista.radio_random.config(command=self.cambiarcolor)
        #self.vista.boton_cerrar.config(command=self.cerrar)
        self.vista.boton_pdf.config(command=self.hacerPDF)
        #self.vista.boton_excel.config(command=self.hacerExcel)
        self.vista.boton_fake.config(command=self.crearFakes)

#-----------------Funciones enlace ---------------------------------

    def clear(self):
        self.modelo.limpiar(self.vista.titulo_var,self.vista.descripcion_var)

    def altaDatos(self):
        self.modelo.ingresodatos(self.vista.titulo_var, self.vista.descripcion_var)
        self.modelo.consultar(self.vista.tree)

    def consultaDatos(self):
        self.modelo.consultar(self.vista.tree)

    def modificar(self):
        seleccion = self.vista.tree.item(self.vista.tree.focus())
        self.modelo.actualizar(seleccion, self.vista.titulo_var,
        self.vista.descripcion_var)
        self.modelo.consultar(self.vista.tree)

    def baja(self):
        seleccion = self.vista.tree.item(self.vista.tree.focus())
        self.modelo.eliminar(seleccion)
        self.modelo.consultar(self.vista.tree)

    def cambiarcolor(self,):
        self.vista.root["bg"]=elegirTema(self.vista.tema_var)
        self.vista.miFrame["bg"]=elegirTema(self.vista.tema_var)
        self.vista.sec_sup["bg"]=elegirTema(self.vista.tema_var)
        self.vista.sec_int["bg"]=elegirTema(self.vista.tema_var)
        self.vista.sec_inf["bg"]=elegirTema(self.vista.tema_var)
        #self.vista.label_titulo["bg"] = elegirTema(self.vista.tema_var)
        self.vista.label1["bg"] = elegirTema(self.vista.tema_var)
        self.vista.label2["bg"] = elegirTema(self.vista.tema_var)
        self.vista.radio_white["bg"] = elegirTema(self.vista.tema_var)
        self.vista.radio_black["bg"] = elegirTema(self.vista.tema_var)
        self.vista.radio_random["bg"] = elegirTema(self.vista.tema_var)

    def hacerPDF(self):
        self.modelo.generar_pdf()

    #def hacerExcel(self):
        #print_excel()

    def crearFakes(self):
        self.modelo.fake()
        self.modelo.consultar(self.vista.tree)

    #def cerrar(self,):
        #self.modelo.salir_aplicacion(self.vista.root)




if __name__ == "__main__":
    window = Tk()
    application = Controller(window)
    mainloop()

###Pendientes relevantes:

#Decoradores:
    #No se aplique el decorador cuando no se valide alta, baja y modificación



###Pendientes no relevantes:
#peewee:
  #Generar xls con peewee
  #PDF acomodarlo con el formato

#Consulta si desea eliminar los datos
#Hacer correr programa desde app
#función Cerrar app desde el model
#Top level para modificar
#Menu superior
#Menu desplegable de los temas
#Importar datos
#Exportar TXT,word, etc