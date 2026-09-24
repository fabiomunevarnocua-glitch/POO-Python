

import tkinter as tk


# Esta clase representa a la persona que puede iniciar sesión.
"""CLASE USUARIO"""
class Usuario:
    # Guarda el usuario y la contraseña permitidos.
    def __init__(self):
        self.__usuario = "admin"
        self.__password = "password"

    # Comprueba si los datos escritos coinciden con los guardados.
    def validar(self, usuario, password):
        return usuario == self.__usuario and password == self.__password


# Esta clase representa un auto dentro del autolavado.
"""CLASE AUTOLAVADO"""
class Autolavado:
    # Crea un auto con su placa, hora de llegada y tarifa.
    def __init__(self, placa, hora_llegada):
        self.__placa = placa
        self.__hora_llegada = hora_llegada
        self.__hora_salida = ""
        self.__tarifa = 20000

    # Guarda la hora en la que el auto sale del autolavado.
    def registrar_salida(self, hora_salida):
        self.__hora_salida = hora_salida

    # Devuelve el valor que debe pagar el cliente.
    def calcular_pago(self):
        return self.__tarifa

    # Devuelve la placa del auto.
    def obtener_placa(self):
        return self.__placa

    # Devuelve la hora de llegada del auto.
    def obtener_hora_llegada(self):
        return self.__hora_llegada

    # Devuelve la hora de salida del auto.
    def obtener_hora_salida(self):
        return self.__hora_salida


# Se crea el usuario que se usará para validar el inicio de sesión.
"""CREAR OBJETO USUARIO"""
usuario = Usuario()


# Aquí se guardan todos los objetos de tipo Autolavado.
"""LISTA DE AUTOS"""
autos = []


# Revisa que la hora no esté vacía.
"""FUNCION VALIDAR HORA"""
def validar_hora(hora):

    if hora == "":
        return False
    else:
        return True


# Comprueba el usuario y abre la ventana principal si los datos son correctos.
"""FUNCION INICIO DE SESION"""
def login():

    if usuario.validar(txt_usuario.get(), txt_password.get()):
        ventana.destroy()
        abrir_autolavado()

    else:
        lbl_resultado.config(text="Usuario o contraseña incorrectos", fg="red")


# Toma los datos escritos y crea un nuevo auto.
"""FUNCION REGISTRAR INGRESO"""
def registrar_ingreso():

    placa = txt_placa.get().upper()
    hora_llegada = txt_llegada.get()

    if placa == "" or hora_llegada == "":
        lbl_mensaje.config(text="Debe llenar todos los campos", fg="red")

    elif validar_hora(hora_llegada) == False:
        lbl_mensaje.config(text="Hora incorrecta. Ejemplo: 08:30", fg="red")

    else:
        auto = Autolavado(placa, hora_llegada)
        autos.append(auto)

        actualizar_lista()

        lbl_mensaje.config(text="Auto registrado correctamente", fg="green")

        txt_placa.delete(0, tk.END)
        txt_llegada.delete(0, tk.END)


    # Registra la salida del auto seleccionado en la lista.
"""FUNCION REGISTRAR SALIDA"""
def registrar_salida():

    seleccion = lista_autos.curselection()

    if seleccion == ():
        lbl_mensaje.config(text="Seleccione un auto de la lista", fg="red")

    else:
        posicion = seleccion[0]
        auto = autos[posicion]

        hora_salida = txt_salida.get()

        if hora_salida == "":
            lbl_mensaje.config(text="Debe ingresar la hora de salida", fg="red")

        elif validar_hora(hora_salida) == False:
            lbl_mensaje.config(text="Hora incorrecta. Ejemplo: 10:30", fg="red")

        elif auto.obtener_hora_salida() != "":
            lbl_mensaje.config(text="Este auto ya tiene registrada la salida", fg="red")

        elif hora_salida <= auto.obtener_hora_llegada():
            lbl_mensaje.config(text="La hora de salida debe ser mayor a la hora de llegada", fg="red")

        else:
            auto.registrar_salida(hora_salida)

            total = auto.calcular_pago()

            actualizar_lista()

            lbl_mensaje.config(text=f"Salida registrada. Total a pagar: ${total}", fg="green")

            txt_salida.delete(0, tk.END)


# Vuelve a mostrar todos los autos con su estado y valor a pagar.
"""FUNCION ACTUALIZAR LISTA"""
def actualizar_lista():

    lista_autos.delete(0, tk.END)

    for auto in autos:

        placa = auto.obtener_placa()
        llegada = auto.obtener_hora_llegada()
        salida = auto.obtener_hora_salida()

        if salida == "":
            estado = "En lavado"
            total = 0

        else:
            estado = "Finalizado"
            total = auto.calcular_pago()

        # Agrega la información del auto como una fila de texto.
        lista_autos.insert(tk.END, f"Placa: {placa} | Llegada: {llegada} | Salida: {salida} | Estado: {estado} | Total: ${total}")


    # Crea la ventana donde se registran los autos y sus salidas.
"""FUNCION ABRIR AUTOLAVADO"""
def abrir_autolavado():

    global txt_placa
    global txt_llegada
    global txt_salida
    global lista_autos
    global lbl_mensaje

    # Esta ventana contiene los controles del autolavado.
    ventana_auto = tk.Tk()
    ventana_auto.title("AUTOLAVADO")
    ventana_auto.geometry("800x600")
    ventana_auto.configure(bg="lightblue")

    # Campo para escribir la placa del auto.
    tk.Label(ventana_auto, text="Placa:", font=("Arial", 14), fg="blue", bg="lightblue").pack()
    txt_placa = tk.Entry(ventana_auto, font=("Arial", 12))
    txt_placa.pack()

    # Fila que contiene la hora de llegada y su aviso.
    marco_llegada = tk.Frame(ventana_auto, bg="lightblue")
    marco_llegada.pack()
    # Texto y campo para escribir la hora de llegada.
    tk.Label(marco_llegada, text="Hora de llegada:", font=("Arial", 14), fg="blue", bg="lightblue").pack(side=tk.LEFT)
    txt_llegada = tk.Entry(marco_llegada, font=("Arial", 12))
    txt_llegada.pack(side=tk.LEFT)
    # Indica el formato esperado para la hora.
    tk.Label(marco_llegada, text="Formato 24 horas (HH:MM)", bg="lightblue").pack(side=tk.LEFT, padx=8)

    # Botón que registra el ingreso del auto.
    tk.Button(ventana_auto, text="Registrar ingreso", font=("Arial", 12), fg="blue", command=registrar_ingreso).pack(pady=10)

    # Título y lista donde se muestran los autos registrados.
    tk.Label(ventana_auto, text="Autos registrados", font=("Arial", 14, "bold"), fg="blue", bg="lightblue").pack()

    lista_autos = tk.Listbox(ventana_auto, width=90, height=10, font=("Arial", 10))
    lista_autos.pack(pady=10)

    # Fila que contiene la hora de salida y su aviso.
    marco_salida = tk.Frame(ventana_auto, bg="lightblue")
    marco_salida.pack()
    # Texto y campo para escribir la hora de salida.
    tk.Label(marco_salida, text="Hora de salida:", font=("Arial", 14), fg="red", bg="lightblue").pack(side=tk.LEFT)
    txt_salida = tk.Entry(marco_salida, font=("Arial", 12))
    txt_salida.pack(side=tk.LEFT)
    # Indica el formato esperado para la hora.
    tk.Label(marco_salida, text="Formato 24 horas (HH:MM)", bg="lightblue").pack(side=tk.LEFT, padx=8)

    # Botón que registra la salida del auto seleccionado.
    tk.Button(ventana_auto, text="Registrar salida", font=("Arial", 12), fg="blue", command=registrar_salida).pack(pady=10)

    # Etiqueta donde se muestran mensajes para el usuario.
    lbl_mensaje = tk.Label(ventana_auto, text="", font=("Arial", 12), bg="lightblue")
    lbl_mensaje.pack()

    ventana_auto.mainloop()


# Crea la primera ventana, donde se escriben las credenciales.
"""CREAR VENTANA LOGIN"""
ventana = tk.Tk()
ventana.title("Autolavado")
ventana.geometry("600x400")
ventana.configure(bg="lightblue")





# Campo para escribir el nombre del usuario.
"""USUARIO"""
tk.Label(ventana, text="Usuario:", font=("Arial", 14), fg="blue", bg="lightblue").pack()
txt_usuario = tk.Entry(ventana)
txt_usuario.pack()


# Campo para escribir la contraseña, que se muestra con asteriscos.
"""PASSWORD"""
tk.Label(ventana, text="Password:", font=("Arial", 14), fg="red", bg="lightblue").pack()
txt_password = tk.Entry(ventana, show="*")
txt_password.pack()


# Botón que ejecuta la función de inicio de sesión.
"""BOTON INGRESAR"""
tk.Button(ventana, text="Ingresar", font=("Arial", 12), fg="blue", command=login).pack(pady=10)


# Etiqueta donde se muestran los mensajes del inicio de sesión.
"""RESULTADO"""
lbl_resultado = tk.Label(ventana, text="", bg="lightblue")
lbl_resultado.pack()

ventana.mainloop()