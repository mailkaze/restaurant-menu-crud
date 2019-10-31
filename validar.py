
def validar_vacio(dato):
    #comprobar que no esté vacío
    if dato is not '':
        return dato
    else:
        return None

def validar_float(dato):
    #que sea un numero float o entero
    try:
        return float(dato)
    except ValueError:
        return None

def validar_entero(dato):
    #que sea un numero entero
    try:
        return int(dato)
    except ValueError:
        return None