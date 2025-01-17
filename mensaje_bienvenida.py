''' Crea un script que dado un nombre de usuario le de la binvenida con su nombre en el formato correcto. '''

# --- PEDIR NOMBRE DE USUARIO ---
# print("¿Cómo te llamas?")
# nombre = input()
nombre = input("¿Cómo te llamas? ") # de tipo string

# --- REFORMATEAMOS EL NOMBRE ---
nombre = nombre.replace(".", "")

# --- ESCRIBIMOS MENSAJE EN UNA VARIABLE / AÑADIMOS FUNCIÓN PARA FORMATEAR EL NOMBRE CORRECTAMENTE ---
mensaje = "¡Hola, " + nombre.title() + ", estás usando Python!"

# --- IMPRIMIMOS EL MENSAJE POR PANTALLA ---
print(mensaje)

# --- EN MAYÚSCULAS ---
print(mensaje.upper())

# --- EN MINÚSCULAS ---
print(mensaje.lower())





