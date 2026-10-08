import json
from pathlib import Path

carpeta_src = Path(__file__).parent
localizacion_usuarios_json = carpeta_src /".."/"Almacenamiento"/"usuarios.json"
localizacion_libros_json = carpeta_src /".."/"Almacenamiento"/"libros.json"

class Usuario():
    def __init__(self):
        pass


class Biblioteca():
    def __init__(self):
        pass
    def prestar_libro(self):
            usuario_encontrado = False
            libro_encontrado = False
            with open(localizacion_usuarios_json, "r", encoding="utf-8") as archivo:
                lista_usuarios = json.load(archivo)
            with open(localizacion_libros_json, "r", encoding="utf-8") as archivo:
                lista_libros = json.load(archivo)

            nombre_usuario = input("Dime el nombre del usuario\n")

            for usuario in lista_usuarios:
                for nombre in usuario:
                    if nombre == nombre_usuario:
                        datos_usuario = usuario #datos con los que trabajar el usuario
                        usuario_encontrado = True
                        break

            if usuario_encontrado:
                titulo_libro = input("Dime el titulo del libro\n")
                for libro in lista_libros:
                    for titulo in libro:
                        if titulo == titulo_libro:
                            datos_libro = libro #datos con los que trabajar el libro
                            libro_encontrado = True
                            break
            else:
                print("El usuario no ha sido en contrado en la base de datos")

            if libro_encontrado:
                #guardado libro
                if datos_libro[titulo_libro][2] == "Disponible":
                    datos_libro[titulo_libro][2] = "No disponible"
                    with open(localizacion_libros_json, "w", encoding="utf-8") as archivo:
                        json.dump(lista_libros, archivo, indent=4)
                    #guardado usuario
                    datos_usuario[nombre_usuario][0].append(titulo_libro)
                    with open(localizacion_usuarios_json, "w", encoding="utf-8") as archivo:
                        json.dump(lista_usuarios, archivo, indent=4)
                else:
                    print(f'El libro "{titulo_libro}" ya lo tiene un usuario, espera hasta que lo devuelva')
            else:
                print(f'El libro "{titulo_libro}" no existe en la base de datos')
                
    def devolver_libro(self):
        #variables de comprobacion
        usuario_encontrado = False
        libro_encontrado = False
        #guardamos los json en variables
        with open(localizacion_usuarios_json, "r", encoding="utf-8") as archivo:
            lista_usuarios = json.load(archivo)
        with open(localizacion_libros_json, "r", encoding="utf-8") as archivo:
            lista_libros = json.load(archivo)

        #pedimos nombre de usuario y validamos su existencia
        nombre_usuario = input("Escribe el nombre del usuario\n")

        #recorremos la lista de usuarios para encontrar el usuario que queremos

        for usuario in lista_usuarios:
            for nombre in usuario: #repetimos for para recorrer el diccionario 'usuario'
                if nombre == nombre_usuario:
                    usuario_encontrado = True
                    datos_usuario = usuario
                    break
        if usuario_encontrado:
            #pedimos el libro
            print("Esta es la lista de libros del usuario")
            for libros_usuario in datos_usuario[nombre_usuario][0]:
                print(f"-{libros_usuario}")
            titulo_libro = input("Escribe el nombre del libro que desea devolver\n")

            for libro in lista_libros:
                for titulo in libro:
                    if titulo_libro == titulo:
                        datos_libro = libro
                        libro_encontrado = True
                        break
            if libro_encontrado:
                for datos in datos_usuario[nombre_usuario][0]:
                    if titulo_libro == datos:
                        libro_en_usuario = True
                        break
                if libro_en_usuario == True:
                    datos_usuario[nombre_usuario][0].remove(titulo_libro)
                    with open(localizacion_usuarios_json, "w", encoding="utf-8") as archivo:
                        json.dump(lista_usuarios, archivo, indent=4)
                    datos_libro[titulo_libro][2] = "Disponible"
                    with open(localizacion_libros_json, "w", encoding="utf-8") as archivo:
                        json.dump(lista_libros, archivo, indent=4)
                else:
                    print("Este libro no esta el la lista de libros del usuario")
            else:
                print("Este libro no ha sido encontrado en la base de datos")
        else:
            print("El usuario no ha sido en contrado en la base de datos")
        
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

    def mostrar_libros(self):
        with open(localizacion_libros_json, "r")as archivo:
            lista_libros = json.load(archivo)
        for libros in lista_libros:
            for datos_libros in libros:
                print(f"-{datos_libros}")
                for claves_datos_libros in libros[datos_libros]:
                    print(f"  -{claves_datos_libros}")
        
            
class Libro():
    def __init__(self, titulo, autor, ID_libro):
        self.titulo = titulo
        self.autor = autor
        self.ID_libro = ID_libro

    def añadir_libro(self):
        dic_libros = {}
        libro = True
        encontrado = False
        disponible = True
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
            if disponible:
                lista_libros.append(dic_libros)
                dic_libros[titulo_libro] = (autor_libro, Id_del_libro, "Disponible")
                with open(localizacion_libros_json, "w", encoding="utf-8") as archivo:
                    json.dump(lista_libros, archivo, indent=4)