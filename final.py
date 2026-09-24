import tkinter


# ==================================================
# EXCEPCIÓN PERSONALIZADA
# ==================================================

class HoraSalidaInvalidaError(Exception):
    pass


# ==================================================
# CLASE USUARIO
# ==================================================

class Usuario:

    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password

    def validar(self, usuario_ingresado, password_ingresada):

        if usuario_ingresado == self.__usuario and password_ingresada == self.__password:
            return True
        else:
            return False


# ==================================================
# CLASE AUTO
# ==================================================

class Auto:

    def __init__(self, placa, hora_llegada, tarifa):
        self.__placa = placa
        self.__hora_llegada = hora_llegada
        self.__hora_salida = None
        self.__tarifa = tarifa

    def registrar_salida(self, hora_salida):

        # Verificamos si ya había salido
        if self.__hora_salida is not None:
            raise HoraSalidaInvalidaError(
                "Este vehículo ya tiene una salida registrada."
            )

        # La salida debe ser mayor que la llegada
        if hora_salida <= self.__hora_llegada:
            raise HoraSalidaInvalidaError(
                "La hora de salida debe ser mayor a la hora de llegada."
            )

        self.__hora_salida = hora_salida

    def calcular_pago(self):

        tiempo = self.__hora_salida - self.__hora_llegada
        pago = tiempo * self.__tarifa

        return pago

    def obtener_placa(self):
        return self.__placa

    def obtener_hora_llegada(self):
        return self.__hora_llegada

    def obtener_hora_salida(self):
        return self.__hora_salida

    def obtener_tarifa(self):
        return self.__tarifa


# ==================================================
# CLASE AUTOLAVADO
# ==================================================

class Autolavado:

    def __init__(self):
        self.__autos = []

    def registrar_auto(self, placa, hora_llegada, tarifa):

        auto = Auto(placa, hora_llegada, tarifa)

        self.__autos.append(auto)

    def obtener_autos(self):
        return self.__autos

    def obtener_auto(self, posicion):
        return self.__autos[posicion]


# ==================================================
# OBJETOS PRINCIPALES
# ==================================================

usuario = Usuario("programacion", "programacion")

sistema = Autolavado()


# ==================================================
# VENTANA PRINCIPAL
# ==================================================

ventana = tkinter.Tk()

ventana.title("Sistema Autolavado")
ventana.geometry("600x450")


# ==================================================
# FRAME DEL LOGIN
# ==================================================

frame_login = tkinter.Frame(ventana)
frame_login.pack(pady=50)


tkinter.Label(
    frame_login,
    text="INICIO DE SESIÓN",
    font=("Arial", 16)
).grid(row=0, column=0, columnspan=2, pady=10)


tkinter.Label(
    frame_login,
    text="Usuario:"
).grid(row=1, column=0)


entrada_usuario = tkinter.Entry(frame_login)

entrada_usuario.grid(
    row=1,
    column=1
)


tkinter.Label(
    frame_login,
    text="Contraseña:"
).grid(row=2, column=0)


entrada_password = tkinter.Entry(
    frame_login,
    show="*"
)

entrada_password.grid(
    row=2,
    column=1
)


resultado_login = tkinter.Label(
    frame_login,
    text=""
)

resultado_login.grid(
    row=4,
    column=0,
    columnspan=2
)


# ==================================================
# MOSTRAR SISTEMA AUTOLAVADO
# ==================================================

def mostrar_autolavado():

    # Borramos el login
    frame_login.destroy()

    frame_auto = tkinter.Frame(ventana)

    frame_auto.pack(pady=20)


    # ------------------------------------------
    # TÍTULO
    # ------------------------------------------

    tkinter.Label(
        frame_auto,
        text="AUTOLAVADO",
        font=("Arial", 16)
    ).grid(
        row=0,
        column=0,
        columnspan=3,
        pady=10
    )


    # ------------------------------------------
    # PLACA
    # ------------------------------------------

    tkinter.Label(
        frame_auto,
        text="Placa:"
    ).grid(row=1, column=0)


    entrada_placa = tkinter.Entry(frame_auto)

    entrada_placa.grid(
        row=1,
        column=1
    )

    def convertir_mayuscula(event):
        texto = entrada_placa.get()
        entrada_placa.delete(0, tkinter.END)
        entrada_placa.insert(0, texto.upper())


    entrada_placa.bind("<KeyRelease>", convertir_mayuscula)
    
    # ------------------------------------------
    # HORA LLEGADA
    # ------------------------------------------

    tkinter.Label(
        frame_auto,
        text="Hora llegada:"
    ).grid(row=2, column=0)


    entrada_llegada = tkinter.Entry(frame_auto)

    entrada_llegada.grid(
        row=2,
        column=1
    )


    # ------------------------------------------
    # TARIFA
    # ------------------------------------------

    """tkinter.Label(
        frame_auto,
        text="Tarifa por hora:"
    ).grid(row=3, column=0)


    entrada_tarifa = tkinter.Entry(frame_auto)

    entrada_tarifa.grid(
        row=3,
        column=1
    )"""


    # ------------------------------------------
    # LISTA DE AUTOS
    # ------------------------------------------

    lista_autos = tkinter.Listbox(
        frame_auto,
        width=50,
        height=8
    )

    lista_autos.grid(
        row=5,
        column=0,
        columnspan=3,
        pady=15
    )


    # ------------------------------------------
    # MENSAJES
    # ------------------------------------------

    resultado = tkinter.Label(
        frame_auto,
        text=""
    )

    resultado.grid(
        row=9,
        column=0,
        columnspan=3,
        pady=10
    )


    # ==========================================
    # ACTUALIZAR LISTA
    # ==========================================

    def actualizar_lista():

        lista_autos.delete(0, tkinter.END)

        autos = sistema.obtener_autos()

        for auto in autos:

            if auto.obtener_hora_salida() is None:

                texto = (
                    auto.obtener_placa()
                    + " - Entrada: "
                    + str(auto.obtener_hora_llegada())
                )

            else:

                pago = auto.calcular_pago()    
                texto = (
                    auto.obtener_placa()
                    + " - Entrada: "
                    + str(auto.obtener_hora_llegada())
                    + " - Salida: "
                    + str(auto.obtener_hora_salida())
                    + " - Total: $"
                    + str(pago)
                )

            lista_autos.insert(
                tkinter.END,
                texto
            )


    # ==========================================
    # REGISTRAR AUTO
    # ==========================================

    def registrar_auto():

        try:

            placa = entrada_placa.get()

            hora_llegada = int(
                entrada_llegada.get()
            )

            tarifa = 20000

            """tarifa = float(
                entrada_tarifa.get()
            )"""


            if placa == "":
                raise ValueError(
                    "Debe ingresar una placa."
                )


            if hora_llegada < 0 or hora_llegada > 23:
                raise ValueError(
                    "La hora debe estar entre 0 y 23."
                )


            """if tarifa <= 0:
                raise ValueError(
                    "La tarifa debe ser mayor que cero."
                )"""


            sistema.registrar_auto(
                placa,
                hora_llegada,
                tarifa
            )


        except ValueError as error:

            resultado.config(
                text="Error: " + str(error)
            )


        else:

            resultado.config(
                text="Vehículo registrado correctamente."
            )

            actualizar_lista()

            entrada_placa.delete(
                0,
                tkinter.END
            )

            entrada_llegada.delete(
                0,
                tkinter.END
            )

            """entrada_tarifa.delete(
                0,
                tkinter.END
            )"""


    # ------------------------------------------
    # BOTÓN REGISTRAR
    # ------------------------------------------

    boton_registrar = tkinter.Button(
        frame_auto,
        text="Registrar auto",
        command=registrar_auto
    )

    boton_registrar.grid(
        row=4,
        column=1,
        pady=10
    )


    # ==========================================
    # HORA DE SALIDA
    # ==========================================

    tkinter.Label(
        frame_auto,
        text="Hora salida:"
    ).grid(row=6, column=0)


    entrada_salida = tkinter.Entry(
        frame_auto
    )

    entrada_salida.grid(
        row=6,
        column=1
    )


    # ==========================================
    # REGISTRAR SALIDA
    # ==========================================

    def registrar_salida():

        try:

            seleccion = lista_autos.curselection()


            if len(seleccion) == 0:

                raise ValueError(
                    "Debe seleccionar un vehículo."
                )


            posicion = seleccion[0]


            auto = sistema.obtener_auto(
                posicion
            )


            hora_salida = int(
                entrada_salida.get()
            )


            if hora_salida < 0 or hora_salida > 23:

                raise HoraSalidaInvalidaError(
                    "La hora debe estar entre 0 y 23."
                )


            auto.registrar_salida(
                hora_salida
            )


            pago = auto.calcular_pago()


        except ValueError as error:

            resultado.config(
                text="Error: " + str(error)
            )


        except HoraSalidaInvalidaError as error:

            resultado.config(
                text="Error: " + str(error)
            )


        else:

            resultado.config(
                text=
                "Placa: "
                + auto.obtener_placa()
                + " - Total a pagar: $"
                + str(pago)
            )

            actualizar_lista()

            entrada_salida.delete(
                0,
                tkinter.END
            )


    # ------------------------------------------
    # BOTÓN SALIDA
    # ------------------------------------------

    boton_salida = tkinter.Button(
        frame_auto,
        text="Registrar salida",
        command=registrar_salida
    )

    boton_salida.grid(
        row=7,
        column=1,
        pady=10
    )


# ==================================================
# FUNCIÓN LOGIN
# ==================================================

def ingresar():

    usuario_ingresado = entrada_usuario.get()

    password_ingresada = entrada_password.get()


    if usuario.validar(
        usuario_ingresado,
        password_ingresada
    ):

        mostrar_autolavado()

    else:

        resultado_login.config(
            text="Acceso denegado"
        )


# ==================================================
# BOTÓN LOGIN
# ==================================================

boton_ingresar = tkinter.Button(
    frame_login,
    text="Ingresar",
    command=ingresar
)

boton_ingresar.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)


# ==================================================
# MANTENER VENTANA ABIERTA
# ==================================================

ventana.mainloop()