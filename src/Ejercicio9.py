def limpiar_nombres(students):
    lista_estudiantes = []
    for alumno in students:
        nombre_limpio = str(alumno["name"]).strip()
        if (nombre_limpio) and (nombre_limpio != 'None'):
            lista_estudiantes.append(alumno)
    return lista_estudiantes

def limpiar_notas(studentsv2):
    lista_estudiantes2 = []
    for alumno in studentsv2:
        try:
            alumno['grade'] = float(alumno['grade'])
        except AttributeError:
            alumno['grade'] = ''
        except TypeError:
            alumno["grade"] = ""
        except ValueError:
            alumno["grade"] = ""
        if (type(alumno["grade"]) is float) and alumno["grade"]:
            lista_estudiantes2.append(alumno)
    return lista_estudiantes2

def normalizar_nombres(studentsv3):
    for alumno in studentsv3:
        alumno["name"] = alumno["name"].strip().title()
        alumno["status"] = alumno["status"].strip().title()
    return studentsv3

def eliminar_duplicados(studentsv4):
    listado = {}
    for alumno in studentsv4:
        nombre = alumno['name']
        nota = alumno['grade']
        if(nombre not in listado) or nota>listado[nombre]['grade']:
            listado[nombre] = alumno
    return list(listado.values())
