import tkinter
from struct import pack
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from tkinter.font import Font



lista_nombre=[]
lista_codigo=[]
lista_nombre1=[]
lista_codigo1=[]
lista_carrera=[]
lista_carrera1=[]
lista_materia=[]
lista_materia1=[]
lista_codigo2=[]
lista_codigo3=[]

class Product2:


    def __init__(self,window2):

        def abrirventana():
            window2.destroy()
            nuevaventana = FrmMenuPrincipal()
            nuevaventana.mainloop()
        def validation3():
            return len(self.combo.get()) != 0 and len(self.miMateria.get()) != 0
        def validation4():
            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])
            return len(values) != 0
        def MODIFICAR():
           if validation4():
            global selected_item,values,combo
            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])

            global ventana2,codigo_nuevo1,carrera_nuevo,materia_nueva,lista_carrera1
            ventana2 = tkinter.Toplevel()
            ventana2.title("Editar datos")
            #Codigo Actual
            Label(ventana2,text="Código actual").grid(row = 0, column = 1)
            Entry(ventana2,textvariable = StringVar(ventana2, value = values[0]),state ="readonly").grid(row = 0,column=2)
            #Codigo Nuevo
            Label(ventana2, text = "Código Nuevo").grid(row = 1,column = 1)
            codigo_nuevo1 = Entry(ventana2)
            codigo_nuevo1.grid(row = 1, column = 2)
            #Carrera Actual

            Label(ventana2, text = "Carrera actual").grid(row =2,column = 1)
            Entry(ventana2, textvariable=StringVar(ventana2, value =values[1] ),state="readonly").grid(row =2,column = 2)
            #Carrera Nueva
            Label(ventana2,text= "Carrera Nueva").grid(row = 3, column=1)
            combo = ttk.Combobox(ventana2, width=17)
            combo.grid(row=3, column=2)
            combo["values"] = ["Sistemas", "Administración", "Ingenieria Industrial", "Ingenieria Ambiental",
                               "Derecho"]
            combo.bind("<<ComboboxSelected>>")
            for string in lista_carrera1:
                if string not in combo['values']:
                    combo['values'] += (string,)
            for string in lista_nombre1:
                if string not in combo['values']:
                    combo['values'] += (string,)

            #Materia Actual
            Label(ventana2, text="Materia actual").grid(row=4, column=1)
            Entry(ventana2, textvariable=StringVar(ventana2, value=values[2]), state="readonly").grid(row=4, column=2)
            #Materia Nueva
            Label(ventana2, text="Materia Nueva").grid(row=5, column=1)
            materia_nueva = Entry(ventana2)
            materia_nueva.grid(row=5, column=2)
            Button(ventana2, text="Guardar", command=guardando1).grid(row=6, column=2, sticky=W)
            my_texto2.set("Modifique los datos que crea necesario")

           else:
            messagebox.showinfo(message="No seleccionó ningun dato de la Tabla", title="Error")


        def guardando1():
           global lista_codigo2
           global lista_carrera1
           global lista_materia1
           global lista_codigo3,combo
           print(values)

           x = values[1]
           y = values[2]
           r = values[0]
           self.tree.delete(selected_item)

           for i in range(len(lista_carrera1)):
               try:
                   if   values[1] == lista_carrera1[i]:
                       global e
                       e = lista_carrera1.index(lista_carrera1[i])




               except:
                   print("")

           try:

               Valor11 = codigo_nuevo1.get()
               Valor12 = combo.get()
               Valor13 = materia_nueva.get()
               lista_codigo3[e]=Valor11
               lista_carrera1[e]= Valor12
               lista_materia1[e] = Valor13




           except:
               print("")



           self.tree.insert('', 0, values=(Valor11,Valor12,Valor13, "Habilitado"))
           ventana2.destroy()

           my_texto2.set("Se modificó Código: '{}' -  Carrera: '{}' y Materia: '{}' a Código: '{}' - Carrera: '{}' y Materia: '{}'  de la Tabla".format(r,x, y,Valor11,Valor12,Valor13))

        def ELIMINAR():
           if validation4():
            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])
            x = values[1]
            y = values[2]



            for i in range(len(lista_carrera1)):
               try:
                if values[1] == lista_carrera1[i] and int(values[0]) == int(lista_codigo3[i]) and values[2] == lista_materia1[i]:
                    d = lista_carrera1.index(lista_carrera1[i])
                    lista_carrera1.pop(int(d))
                    lista_materia1.pop(int(d))
                    lista_codigo3.pop(int(d))

               except:
                   print("")



            self.tree.delete(selected_item)

            my_texto2.set("Se eliminaron a Carrera: '{}' y Materia: '{}'  de la Tabla".format(x, y))

           else:
            messagebox.showinfo(message="No seleccionó ningun dato de la Tabla", title="Error")
        def GRABAR(carrera,materia):
           if validation3():

            lista_materia.append(materia)

            lista_materia1.append(materia)
            lista_carrera.append(carrera)
            lista_carrera1.append(carrera)




            global m,lista_codigo3


            try:
             for i in range(len(lista_carrera1)):
                 m = len(lista_carrera1)
                 self.tree.insert('', i, values=(m, lista_carrera[i], lista_materia[i], "Habilitado"))
                 lista_codigo3.append(m)
                 print(lista_codigo3)
                 lista_materia.clear()
                 lista_carrera.clear()



            except:
                print("")

            self.materia.set("")
            self.var1.set("")

            my_texto2.set("Carrera: '{}' y Materia: '{}' fueron agregados con éxito".format(carrera, materia))

           else:
            messagebox.showinfo(message="Carrera y Materia son campos requeridos", title="Error")
        global lista_codigo2
        global lista_materia1
        global lista_carrera1


        self.wind = window2
        self.wind.title("Mantenimiento de las Carreras")
        self.materia=StringVar()
        frame = tkinter.LabelFrame(self.wind, text="Mantenimiento de la Tabla Carrera Profesional")
        frame.grid(row=0, column=0, columnspan=3, pady=50)

        self.miMateria = tkinter.Entry(frame,textvariable=self.materia)

        tkinter.Label(frame, text="Nombre Materia: ").grid(row=3, column=0,pady=6)




        self.miMateria.grid(row=3, column=1,sticky=tkinter.W + tkinter.E)
        tkinter.Label(frame, text="Carrera: ").grid(row=1, column=0)

        self.var1=StringVar()
        self.combo = ttk.Combobox(frame,textvariable=self.var1)
        self.combo.grid(row=1, column=1,sticky=tkinter.W + tkinter.E)
        self.combo["values"] = ["Sistemas", "Administración", "Ingenieria Industrial", "Ingenieria Ambiental","Derecho"]
        self.combo.bind("<<ComboboxSelected>>")
        for string in lista_nombre1:
            if string not in self.combo['values']:
                self.combo['values'] += (string,)
        for string in lista_carrera1:
            if string not in self.combo['values']:
                self.combo['values'] += (string,)



        f = int(len(lista_carrera1))
        global my_texto2
        my_texto2 = StringVar()
        ttk.Button(frame, text="Grabar", command=lambda: GRABAR(self.combo.get(),self.miMateria.get())).grid(row=6,
                                                                                                                columnspan=2,
                                                                                                                sticky=tkinter.W + tkinter.E)
        ttk.Button(frame, text="Modificar", command=MODIFICAR).grid(row=4, columnspan=3,pady=2, sticky=tkinter.W)
        ttk.Button(frame, text="Eliminar", command=ELIMINAR).grid(row=4, columnspan=3,pady=2, sticky=tkinter.E)
        self.message = tkinter.Label(frame, textvariable=my_texto2, fg="red").grid(row=7, columnspan=2,
                                                                                  sticky=tkinter.W + tkinter.E)


        # Table
        col = ('Código', 'Carrera','Materia', 'Estado')
        self.tree = ttk.Treeview(height=10, show='headings', columns=(col))
        self.tree.grid(row=4, column=0, columnspan=1)

        self.tree.column('Código', width=80, anchor=tkinter.CENTER)
        self.tree.column('Carrera', width=190, anchor=tkinter.CENTER)
        self.tree.column('Materia', width=190, anchor=tkinter.CENTER)
        self.tree.column('Estado', width=150, anchor=tkinter.CENTER)


        self.tree.heading('Código', text='Código')
        self.tree.heading('Carrera', text='Carrera')
        self.tree.heading('Materia', text='Materia')
        self.tree.heading('Estado', text='Estado')


        btn_font = Font(family="Roboto Cn", size=11)
        boton2 = tk.Button(window2, bg="silver", text=' Regresar ', font=btn_font, width=12, relief="raised",
                           command=abrirventana)
        boton2.place(x=490, y=2)
        btnmant = tkinter.Button(window2, text="Mantenimiento", font=btn_font, width=12, relief="groove")
        btnmant.place(x=4, y=2)
        for i in range(len(lista_carrera1)):

            self.tree.insert('', i,  values=(lista_codigo3[i],lista_carrera1[i],lista_materia1[i], "Habilitado"))

class Product:


    def __init__(self,window):

        def abrirventana():
            window.destroy()
            nuevaventana = FrmMenuPrincipal()
            nuevaventana.mainloop()

        def GRABAR(nombre, codigo):
           if validation():
            lista_nombre.append(nombre)
            lista_codigo.append(codigo)
            lista_nombre1.append(nombre)
            lista_codigo1.append(codigo)




            for i in range(len(lista_nombre)):

              self.tree.insert('',i,values=(lista_codigo[i],lista_nombre[i],"Habilitado"))

              lista_codigo.clear()
              lista_nombre.clear()
            self.usernameVal.set("")
            self.userCode.set("")

            my_texto.set("Nombre: '{}' y Código: '{}' fueron agregados con éxito".format( nombre,codigo ))

           else:
             messagebox.showinfo(message="Código y Nombre son requeridos", title="Error")
        def validation():
            return len(self.miNombre.get()) != 0 and len(self.miCodigo.get()) != 0
        def validation2():
            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])
            return len(values) != 0
        def MODIFICAR():
           if validation2():
            global selected_item,values
            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])

            global ventana2,codigo_nuevo,nombre_nuevo
            ventana2 = tkinter.Toplevel()
            ventana2.title("Editar datos")
            #Codigo Actual
            Label(ventana2,text="Código actual").grid(row = 0, column = 1)
            Entry(ventana2,textvariable = StringVar(ventana2, value = values[0]),state ="readonly").grid(row = 0,column=2)
            #Codigo Nuevo
            Label(ventana2, text = "Código Nuevo").grid(row = 1,column = 1)
            codigo_nuevo = Entry(ventana2)
            codigo_nuevo.grid(row = 1, column = 2)
            #Nombre Actual
            Label(ventana2, text = "Nombre actual").grid(row =2,column = 1)
            Entry(ventana2, textvariable=StringVar(ventana2, value =values[1] ),state="readonly").grid(row =2,column = 2)
            #Nombre Nuevo
            Label(ventana2,text= "Nombre Nuevo").grid(row = 3, column=1)
            nombre_nuevo=Entry(ventana2)
            nombre_nuevo.grid(row = 3,column = 2)
            Button(ventana2,text="Guardar",command= guardando).grid(row =4,column =2,sticky =W)
            my_texto.set("Modifique sólo lo que crea necesario")
           else:
            messagebox.showinfo(message="No seleccionó ningun dato de la Tabla", title="Error")
        def guardando():
           global lista_codigo1
           global lista_nombre1

           x = values[0]
           y = values[1]
           self.tree.delete(selected_item)

           for i in range(len(lista_codigo1)):
               try:
                   if int(values[0]) == int(lista_codigo1[i]) and values[1] == lista_nombre1[i] :
                       global e
                       e = lista_codigo1.index(lista_codigo1[i])



               except:
                   print("")

           try:

               Valor1 = codigo_nuevo.get()
               Valor2 = nombre_nuevo.get()
               lista_codigo1[e]=Valor1
               lista_nombre1[e]= Valor2




           except:
               print("")



           self.tree.insert('', 0, values=(Valor1,Valor2, "Habilitado"))
           ventana2.destroy()
           my_texto.set("Nombre: '{}' y Código: '{}' se cambió a Nombre: '{}' y Codigo: '{}' con éxito".format( x,y,Valor1,Valor2 ))

        def ELIMINAR():
           if validation2():

            selected_item = self.tree.selection()
            values = tuple(self.tree.item(selected_item)['values'])

            w = values[0]
            z = values[1]

            for i in range(len(lista_codigo1)):
               try:
                if int(values[0]) == int(lista_codigo1[i]) and values[1] == lista_nombre1[i] :
                    d = lista_codigo1.index(lista_codigo1[i])
                    lista_codigo1.pop(int(d))
                    lista_nombre1.pop(int(d))


               except:
                   print("")





            self.tree.delete(selected_item)
            my_texto.set("Nombre: '{}' y Código: '{}' eliminados con éxito".format( w,z ))
           else:
            messagebox.showinfo(message="No seleccionó ningun dato de la Tabla", title="Error")





        global lista_carrera
        global lista_materia
        global lista_nombre

        nombre = tkinter.StringVar()
        codigo = tkinter.StringVar()

        self.wind = window
        self.wind.title("Mantenimiento")
        self.usernameVal = StringVar()
        self.userCode = StringVar()
        frame = tkinter.LabelFrame(self.wind, text="Mantenimiento de la Tabla Carrera Profesional")
        frame.grid(row=0, column=0, columnspan=4, pady=50)
        tkinter.Label(frame, text="Nombre: ").grid(row=2, column=0)
        self.miNombre = tkinter.Entry(frame,textvariable= self.usernameVal)
        self.miNombre.focus()
        self.miNombre.grid(row=2, column=1)
        tkinter.Label(frame, text="Código: ").grid(row=1, column=0)
        self.miCodigo = tkinter.Entry(frame,textvariable = self.userCode)
        self.miCodigo.grid(row=1, column=1)
        global my_texto,miNombre
        my_texto = StringVar()
        ttk.Button(frame, text="Grabar",command=lambda: GRABAR(self.miNombre.get(),self.miCodigo.get())).grid(row=3, columnspan=2, sticky=tkinter.W + tkinter.E)
        ttk.Button(frame, text="Modificar", command=MODIFICAR).grid(row=4, columnspan=2, sticky=tkinter.W)
        ttk.Button(frame, text="Eliminar", command=ELIMINAR).grid(row=4, columnspan=2, sticky=tkinter.E)


        self.message = tkinter.Label(frame,textvariable=my_texto,fg="red").grid(row=5,columnspan=2,sticky=tkinter.W + tkinter.E)


        # Table
        col=('Código','Nombre','Estado')
        self.tree = ttk.Treeview(height=10,show='headings', columns=(col))
        self.tree.grid(row=4, column=0, columnspan=1)

        self.tree.column('Código', width=80, anchor=tkinter.CENTER)
        self.tree.column('Nombre', width=190, anchor=tkinter.CENTER)
        self.tree.column('Estado', width=150, anchor=tkinter.CENTER)

        self.tree.heading('Código', text='Código')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Estado', text='Estado')

        btn_font = Font(family="Roboto Cn", size=11)
        boton2 = tk.Button(window, bg="silver", text=' Regresar ', font=btn_font, width=12, relief="raised",
                           command=abrirventana)
        boton2.place(x=300, y=2)
        btnmant = tkinter.Button(window, text="Mantenimiento", font=btn_font, width=12, relief="groove")
        btnmant.place(x=4, y=2)



        try:
         for i in range(len(lista_codigo1)):
            self.tree.insert('', i,  values=(lista_codigo1[i], lista_nombre1[i],"Habilitado"))
        except:
            print("")





class FrmMenuPrincipal(tkinter.Frame):
    def __init__(self):
        global obj_ventana
        obj_ventana = tkinter.Tk()
        super().__init__(obj_ventana)
        obj_ventana.title("Menú de Listado  !!!!")
        obj_ventana.geometry("500x300")
        self.iniciarComponentes()

    def iniciarComponentes(self):
        btn_font = Font(family="Roboto Cn", size=14)
        btnmant = tkinter.Button(obj_ventana, text="Mantenimiento", font=btn_font, width=12, relief="groove")
        btnmant.place(x=4, y=10)

        btnregistrar = tkinter.Button(obj_ventana, text="Carrera Profesional", font=btn_font,width=20,height=4,relief="raised", command=self.registrar)
        btnregistrar.place(x=30, y=100)
        btnlistar = tkinter.Button(obj_ventana, text="Materia", font=btn_font, width=12,height=4, relief="raised",command=self.listar)
        btnlistar.place(x=320, y=100)


    def registrar(self):


        cerrarventana()

        if __name__ == '__main__':
            window = tkinter.Tk()
            application = Product(window)
            window.mainloop()
    def listar(self):


        cerrarventana()
        if __name__ == '__main__':
            window2 = tkinter.Tk()
            application = Product2(window2)
            window2.mainloop()


def cerrarventana():
    obj_ventana.destroy()


objeto = FrmMenuPrincipal()
objeto.mainloop()
