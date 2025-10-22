# Actividad Sesion 5 - Herencia y Excepciones en Python

# Clase base Usuario
class Usuario:
    # Metodo constructor: se ejecuta automaticamente al crear un objeto
    # self representa al propio objeto (como "yo mismo")
    def __init__(self, nombre, correo):
        self.nombre = nombre  # Guarda el nombre del usuario
        self.correo = correo  # Guarda el correo del usuario

    # Metodo para presentarse
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")  # Muestra el nombre del usuario


# Subclase Administrador que hereda de Usuario
class Administrador(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)  # Llama al constructor de Usuario
        self.permisos = []  # Inicializa una lista vacia de permisos

    # Sobrescribe el metodo presentarse
    def presentarse(self):
        print(f"Hola, soy el administrador {self.nombre}. Permisos: {', '.join(self.permisos)}")

    # Metodo para agregar permisos
    def agregar_permiso(self, permiso):
        self.permisos.append(permiso)  # Agrega un nuevo permiso a la lista

    # Metodo para eliminar usuarios
    def eliminar_usuario(self, nombre):
        if nombre not in usuarios_registrados:
            raise UsuarioNoEncontrado(nombre)  # Lanza una excepcion si no se encuentra el usuario
        usuarios_registrados.remove(nombre)  # Elimina el usuario de la lista
        print(f"Usuario '{nombre}' eliminado correctamente.")


# Lista simulada de usuarios
usuarios_registrados = ["cristian", "maria", "juan"]  # Lista que simula una base de datos


# Excepcion personalizada
class UsuarioNoEncontrado(Exception):
    def __init__(self, nombre):
        super().__init__(f"El usuario '{nombre}' no fue encontrado.")  # Mensaje de error personalizado


# Crear objeto administrador
admin = Administrador("Cristian", "cristianjelves01@email.com")  # Crea un administrador
admin.agregar_permiso("eliminar usuarios")  # Le da permiso de eliminar usuarios
admin.presentarse()  # Se presenta mostrando nombre y permisos


# Manejo de excepciones
try:
    admin.eliminar_usuario("pedro")  # Intenta eliminar un usuario que no existe
except UsuarioNoEncontrado as e:
    print(f"Error: {e}")  # Muestra el mensaje de error si ocurre la excepcion
finally:
    print("Operacion de eliminacion finalizada.")  # Siempre se ejecuta


# Herencia multiple
class Soporte:
    def atender(self):
        print("Atendiendo solicitud de soporte...")  # Metodo de la clase Soporte


# Clase SuperUsuario que hereda de Administrador y Soporte
class SuperUsuario(Administrador, Soporte):
    pass  # No se agrega nada nuevo por ahora


# Mostrar el orden de resolucion de metodos
print("\nOrden de resolucion de metodos (MRO) para SuperUsuario:")
print(SuperUsuario.__mro__)  # Muestra el orden en que Python busca los metodos
