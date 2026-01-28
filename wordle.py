### Ingresamos las variables iniciales
cantidad_letras = 5
intentos_maximos = 6
palabra_secreta = "calor"

### Definimos la funcion de verificador de palabra

def verificador_palabra(palabra_ingresada, palabra_secreta):
    ## Creamos la lista de letras verificadas
    letras_verificadas = []

    for i in range(cantidad_letras):
        ## Aca pongo el if para que ponga en [] la letra que esta en la palabra en posicion correcta
        if palabra_ingresada[i] == palabra_secreta[i]:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        ## Aca pongo el if para que ponga en () la letra que esta en la palabra pero en posicion incorrecta
        elif palabra_ingresada[i] in palabra_secreta:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        ## el else para las letras incorrectas
        else:
            letras_verificadas.append(palabra_ingresada[i])
        ## Y por ultimo un return que guarda los valores
    return letras_verificadas

