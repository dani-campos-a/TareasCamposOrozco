import re


def invert_case(cadena):
    regex = re.compile('[^a-zA-Z\s]')
    # Verificar si la entrada es una cadena
    if not isinstance(cadena, str):
        estado = -16
        res1 = None
    else:
        # Verificar si la cadena está vacía
        if not cadena.strip():
            estado = -48
            res1 = None
        # Verificar si la cadena no contiene caracteres alfabéticos
        elif not regex.search(cadena) is None:
            estado = -32
            res1 = None
        else:
            # Invertir el caso de los caracteres
            res1 = ""
            estado = 0
            for char in cadena:
                if char.islower():
                    res1 += char.upper()
                elif char.isupper():
                    res1 += char.lower()
                else:
                    res1 += char

    # Imprimir la cadena original y el resultado
    print("Cadena original:", cadena)
    print("Resultado:", res1)

    return estado, res1



def numero_primo(base):
    result = []  # Cadena vacía para almacenar la lista de primos
    max_sol = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if type(base) is not int: # validar que la base sea un entero
        estado = -64
        result = None

    else:
        # Si la base es un entero valida que no sea mayor a 100
        if base > 100:
            estado = -80
            result = None
        else:

            for i in max_sol:  # Recorre la lista de la maxima solución posible
                if i <= base:  # Si encuentra la base la incluye en la lista y termina
                    result.append(i)

                estado = 0
                max_sol = result
    return estado, result  # Retorna el estado de la operación y resultado
