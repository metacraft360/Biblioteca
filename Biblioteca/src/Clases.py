import json
from pathlib import Path

carpeta_src = Path(__file__).parent
localizacion_usuarios_json = carpeta_src /".."/"Almacenamiento"/"usuarios.json"
localizacion_libros_json = carpeta_src /".."/"Almacenamiento"/"libros.json"

class Usuario():
    def __init__(self, nombre, ID, libros_prestados):
        pass
    def prestar_libro(self):
        with open(localizacion_usuarios_json, "r") as archivo:
            lista_usuarios = json.load(archivo)
        with open(localizacion_libros_json, "r") as archivo:
            lista_libros = json.load(archivo)

        nombre_usuario = input("Cual es el nombre del usuario")

        

class Biblioteca():
    def __init__(self):
        pass
    def registrar_usuario(self):
        libros_prestados = []
        dic_usuarios = {}
        encontrado = False

        with open(localizacion_usuarios_json, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
        nombre_usuario = input("Escribe el nombre de usuario\n")
        id_usuario = input("Escribe el ID del usuario\n")

        for nombres in usuarios:
            if nombre_usuario in nombres:
                encontrado = True
        if encontrado:
            print("Esta cuenta ya existe")
        else:
            usuarios.append(dic_usuarios)
            dic_usuarios[nombre_usuario] = (libros_prestados, id_usuario )
            with open(localizacion_usuarios_json, "w", encoding="utf-8") as archivo:
                json.dump(usuarios, archivo, indent=4)

    def mostrar_clientes(self):
        with open(localizacion_usuarios_json, "r", encoding="utf-8") as archivo:
            usuarios = json.load(archivo)
        for usuario in usuarios:
            for datos_usuario in usuario:
                print(f"-{datos_usuario}")
                for lista_datos_usuario in usuario[datos_usuario]:
                    print(f"  -{lista_datos_usuario}")
        
            
class Libro():
    def __init__(self, titulo, autor, ID_libro):
        self.titulo = titulo
        self.autor = autor
        self.ID_libro = ID_libro

    def añadir_libro(self):
        dic_libros = {}
        libro = True
        encontrado = False
        with open(localizacion_libros_json, "r", encoding="utf-8") as archivo:
            lista_libros = json.load(archivo)
        titulo_libro = input("Escribe el nombre del libro\n")
        autor_libro = input("Escribe el nombre del autor\n")
        while libro:
            try:
                Id_del_libro = int(input("Escribe el ID del libro\n"))
                libro = False
            except ValueError:
                print("Escribe números")

        for libros in lista_libros:
            if titulo_libro in libros:
                encontrado = True

        if encontrado:
            print("Este libro ya esta en la lista de libros")
        else:
            lista_libros.append(dic_libros)
            dic_libros[titulo_libro] = (autor_libro, Id_del_libro)
            with open(localizacion_libros_json, "w", encoding="utf-8") as archivo:
                json.dump(lista_libros, archivo, indent=4)