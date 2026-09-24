
import tkinter


# ---------------- CLASE USUARIO ----------------
class Usuario:

    def __init__(self, usuario, password):
        self.__usuario = usuario
        self.__password = password

    def validar(self, usuario_ingresado, password_ingresada):

        if usuario_ingresado == self.__usuario and password_ingresada == self.__password:
            return True
        else:
            return False


# Creamos el usuario válido
usuario = Usuario("programacion", "programacion")


# ---------------- VENTANA ----------------
ventana = tkinter.Tk()

ventana.title("Inicio de sesión")
ventana.geometry("500x300")


# Texto Usuario
label_usuario = tkinter.Label(ventana, text="Usuario:")
label_usuario.grid(row=0, column=0)


# Caja Usuario
entrada_usuario = tkinter.Entry(ventana)
entrada_usuario.grid(row=0, column=1)


# Texto Contraseña
label_password = tkinter.Label(ventana, text="Contraseña:")
label_password.grid(row=1, column=0)


# Caja Contraseña
entrada_password = tkinter.Entry(ventana, show="*")
entrada_password.grid(row=1, column=1)


# Label donde aparecerá el resultado
resultado = tkinter.Label(ventana, text="")
resultado.grid(row=3, column=1)


# ---------------- FUNCIÓN DEL BOTÓN ----------------
def ingresar():

    usuario_ingresado = entrada_usuario.get()
    password_ingresada = entrada_password.get()

    if usuario.validar(usuario_ingresado, password_ingresada):
        resultado.config(text="Acceso concedido")

    else:
        resultado.config(text="Acceso denegado")


# Botón
boton_ingresar = tkinter.Button(
    ventana,
    text="Ingresar",
    command=ingresar
)

boton_ingresar.grid(row=2, column=1)


# Mantener ventana abierta
ventana.mainloop()