def saludar(nombre):
    """
    Función que saluda a una persona.

    Args:
        nombre: El nombre de la persona a la que se saluda.

    Returns:
        Un mensaje de saludo.
    """
    return f"¡Hola, {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    saludo = saludar(nombre)
    print(saludo)

numero_uno = 5
numero_dos = 25
suma = numero_uno + numero_dos

resta = numero_dos - numero_uno
