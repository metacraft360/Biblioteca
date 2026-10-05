import json
from src.Clases import Usuario, Biblioteca, Libro
mi_biblioteca = Biblioteca()
titulo = ""
autor = ""
id_del_libro = 0
mi_libro = Libro(titulo, autor, id_del_libro)

elegir_accion = True
while elegir_accion:
    try:
        accion = int(input("Elige entre\n(1)Registrar usuario    (2)Añadir libro\n(3)Mostrar clientes    (4)Mostrar libros\n(5)Prestar libro    (6)Devolver libro\n(7)Salir\n\n"))
        if accion == 1:
            mi_biblioteca.registrar_usuario()
        elif accion == 2:
            mi_libro.añadir_libro()
        elif accion == 3:
            mi_biblioteca.mostrar_clientes()
        elif accion == 2:
            pass
        elif accion == 2:
            pass
        elif accion == 2:
            pass
        elif accion == 7:
            elegir_accion = False
        else:
            pass
    except ValueError:
        print("Elige entre 1-7")
