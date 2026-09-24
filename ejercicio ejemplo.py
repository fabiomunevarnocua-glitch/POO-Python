import tkinter as tk
class Usuario:
    def __init__(self):
        self.__usuario = "admin"
        self.__password = "123"

    def validar(self, usuario, password):
       
        return usuario == self.__usuario and password == self.__password
      
        
""""crear objetousuario"""
usuario = Usuario()

"""funcion de inicio de secion"""
def login():

    if usuario.validar(txt_usuario.get(), txt_password.get()):
        lbl_resultado.config(text="Inicio de sesión exitoso", fg="green")

    else:
        lbl_resultado.config(text="Usuario o contraseña incorrectos", fg="red")    


"""crear ventana"""
ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.geometry("600x400")
ventana.configure(bg="lightblue")

titulo = tk.Label(ventana, text="Biblioteca", font=("Arial", 22, "bold"), fg="white", bg="blue")
titulo.pack(pady=10)

tk.Label(ventana, text="Usuario:", font=("Arial", 14), fg="blue",bg="lightblue").pack()
txt_usuario = tk.Entry(ventana)
txt_usuario.pack()

tk.Label(ventana, text="Password:", font=("Arial", 14), fg="red",bg="lightblue").pack()
txt_password = tk.Entry(ventana)
txt_password.pack()

tk.Button(ventana, text="Ingresar", font=("Arial", 12),fg="blue", command=login).pack(pady=10) 

lbl_resultado = tk.Label(ventana, text="",bg="lightblue")
lbl_resultado.pack()

ventana.mainloop()


