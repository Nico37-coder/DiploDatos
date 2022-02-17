import re
from tkinter import messagebox
#from tkinter.messagebox import *



def validar(titulo_var):
  cadena=titulo_var.get()
  patron=("^[A-Za-z]+(?:[ -][A-Za-z]+)*$")
  if(re.match(patron,cadena)):
      #print("Validado")
      return "True"
  else:
      messagebox.showinfo("Error", "Título invalido: " +
            titulo_var.get() +
            "\nNo puede estar vacío, contener números o símbolos")
      print("No validado")
      return "False"

